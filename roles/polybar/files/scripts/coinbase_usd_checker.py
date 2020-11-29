#!/usr/bin/env python

import requests
import ssl

from socket import timeout as socket_timeout
from socket import error as socket_error

URL_COINBASE = "https://api.coinbase.com/v2/prices/spot?currency=USD"

REQUESTS_EXCEPTION = (
    ssl.SSLError,
    requests.exceptions.RequestException,
    socket_error,
    socket_timeout,
)

try:
    response = requests.get(URL_COINBASE)

except REQUESTS_EXCEPTION:
    print("Error")

else:
    print(f"${ response.json()['data']['amount'] }")
