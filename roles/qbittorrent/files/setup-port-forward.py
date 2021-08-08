#! /usr/bin/env python3
# Ansible managed

import sys
import socket
import struct
import base64
import json
import argparse
import logging

import requests

from pathlib import Path
from datetime import datetime

from qbittorrent import Client
from urllib3.exceptions import InsecureRequestWarning


def get_default_vpn_gateway():
    with open("/proc/net/route") as h_proc:
        route_data = h_proc.readlines()

    for line in route_data:
        interface, destination, gateway, _ = line.split(maxsplit=3)

        if interface == "tun0" and destination == "00000000":
            return socket.inet_ntoa(struct.pack("<L", int(gateway, 16)))


def read_payload_cache():
    try:
        with open(CACHE_FILE) as h_cache:
            cache_data = json.load(h_cache)
    except FileNotFoundError:
        return False, "File not Found", ""
    except json.JSONDecodeError:
        return False, "JSON Decode error", ""

    if "payload" not in cache_data or "signature" not in cache_data:
        return False, "payload and/or signature not in file", ""

    return True, cache_data["payload"], cache_data["signature"]


def get_token(pia_username, pia_password):
    try:
        response = requests.get(
            "https://10.0.0.1/authv3/generateToken",
            auth=(pia_username, pia_password),
            verify=False,
        )
    except requests.exceptions.RequestException:
        return False, "Error while connecting to meta server"

    response_data = response.json()

    if response_data["status"] != "OK":
        return False, response_data

    return True, response_data["token"]


def get_payload(gateway, token):
    try:
        response = requests.get(
            f"https://{gateway}:19999/getSignature",
            params={"token": token},
            verify=False,
        )
    except requests.exceptions.RequestException:
        return False, "Error while connecting to gateway for signature."

    response_data = response.json()
    if response_data["status"] != "OK":
        return False, response_data, ""

    return True, response_data["payload"], response_data["signature"]


def bind_port(gateway, payload, signature):
    try:
        response = requests.get(
            f"https://{gateway}:19999/bindPort",
            params={"payload": payload, "signature": signature},
            verify=False,
        )
    except requests.exceptions.RequestException:
        return False, "Error while connecting to gateway for bind."

    response_data = response.json()
    if response_data["status"] != "OK":
        return False, response_data
    return True, response_data["message"]


if __name__ == "__main__":
    CACHE_FILE = Path.joinpath(Path.home(), ".cache", "pia_port_forwarding_cache")

    LOGGER = logging.getLogger()
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s: %(message)s", datefmt="%H:%M %d-%m-%Y"
    )

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Do not output messages.",
        default=False,
    )

    argument_parser.add_argument(
        "--username",
        "-u",
        type=str,
        help="Private Internet Access username",
        required=True,
    )
    argument_parser.add_argument(
        "--password",
        "-p",
        type=str,
        help="Private Internet Access password",
        required=True,
    )

    argument_parser.add_argument(
        "--gateway", "-g", type=str, help="The default VPN gateway IP address"
    )

    argument_parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Do not use payload cache",
        default=False,
    )

    arguments = argument_parser.parse_args()

    if arguments.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    gateway = arguments.gateway or get_default_vpn_gateway()
    if gateway is None:
        logging.error("Could not get default VPN gateway.")
        sys.exit(1)

    if not arguments.no_cache:
        logging.info(f"Reading cache from {CACHE_FILE}")
        cache_success, payload, signature = read_payload_cache()
        if not cache_success and not arguments.quiet:
            logging.warning(f"Error reading cache file: {payload}.")

        if cache_success:
            payload_decoded = json.loads(base64.b64decode(payload))
            expiration_date = datetime.fromisoformat(payload_decoded["expires_at"][:26])
            if expiration_date <= datetime.now():
                logging.warning(f"Expired")
                cache_success = False
    else:
        cache_success = False

    if not cache_success:
        logging.info(f"Requesting new payload and signature.")

        token_success, token_data = get_token(arguments.username, arguments.password)
        if not token_success:
            logging.error(f"Error while getting token: {token_data}.")
            sys.exit(1)

        logging.info(f"Got token: {token_data}")

        payload_success, payload, signature = get_payload(gateway, token_data)
        if not payload_success:
            logging.error(f"Error while getting payload and signature: {payload}.")
            sys.exit(1)

        with open(CACHE_FILE, "w") as h_cache:
            json.dump({"payload": payload, "signature": signature}, h_cache)

    logging.info(f"Payload: {payload}")
    logging.info(f"Signature: {signature}")

    payload_decoded = json.loads(base64.b64decode(payload))
    forwarded_port = payload_decoded["port"]
    logging.info(f"Payload (decoded): {payload_decoded}")
    logging.info(f"Forwarded port: {forwarded_port}")

    bind_success, bind_data = bind_port(gateway, payload, signature)
    if not bind_success:
        logging.error(f"Error while binding port: {bind_data}.")
        sys.exit(1)

    logging.info(f"Port opened successfully: {bind_data}")

    qb = Client("http://127.0.0.1:8080")
    qb.set_preferences(listen_port=forwarded_port)
    listen_port = qb.preferences()["listen_port"]

    if listen_port != forwarded_port:
        logging.error(f"Port not set.")
        sys.exit(1)
    else:
        logging.info(f"Port successfully opened and set.")
