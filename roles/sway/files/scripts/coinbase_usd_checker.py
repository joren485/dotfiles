#!/usr/bin/env python
# Ansible managed

import requests
import sys

URL_BTC = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
URL_ETH = "https://api.coinbase.com/v2/prices/ETH-USD/spot"

try:
    if sys.argv[1] == "btc":
        response = requests.get(URL_BTC)
    elif sys.argv[1] == "eth":
        response = requests.get(URL_ETH)
    else:
        raise ValueError()

    price = round(float(response.json()["data"]["amount"]), 2)
except Exception:
    print("Error")
else:
    print(f"${price}")
