#!/usr/bin/env python
# Ansible managed

import requests
import ssl
import sys

from socket import timeout as socket_timeout
from socket import error as socket_error

URL_BTC = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
URL_ETH = "https://api.coinbase.com/v2/prices/ETH-USD/spot"

try:
    if sys.argv[1] == "btc":
        response = requests.get(URL_BTC)
    elif sys.argv[1] == "eth":
        response = requests.get(URL_ETH)
    else:
        raise ValueError()

except (IndexError, requests.exceptions.RequestException, ValueError):
    print("Error")

else:
    price = response.json()["data"]["amount"]
    print(f"${price}")
