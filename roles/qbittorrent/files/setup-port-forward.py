#! /usr/bin/env python3

import sys
import json
import secrets

import requests

from qbittorrent import Client

URL_PIA_API = "http://209.222.18.222:2000"
URL_QBITTORRENT = "http://127.0.0.1:8080"

PIA_CLIENT_ID = secrets.token_hex(32)

try:
    response_pia = requests.get(f"{URL_PIA_API}/?client_id={PIA_CLIENT_ID}")
except requests.exceptions.RequestException:
    sys.exit("Cannot reach PIA port forwarding API server.")

try:
    pia_data = response_pia.json()
    forwarded_port = pia_data["port"]
except (json.JSONDecodeError, KeyError):
    sys.exit(
        f"Got invalid JSON from PIA port forwarding API server: {response_pia.text}"
    )

qb = Client(URL_QBITTORRENT)
qb.set_preferences(listen_port=forwarded_port)
listen_port = qb.preferences()["listen_port"]

if listen_port != forwarded_port:
    sys.exit("Port not set")

print(f"Successfully set the forwarded port to {forwarded_port}")
