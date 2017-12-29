#!/usr/bin/env python

from socket import timeout as socket_timeout
from socket import error as socket_error

import requests
import ssl

COINBASE_URL = 'https://api.coinbase.com/v2/prices/spot?currency=USD&api=2'

REQUESTS_EXCEPTION = (ssl.SSLError, requests.exceptions.RequestException,
                        socket_error, socket_timeout)

try:
	response = requests.get(COINBASE_URL)

except REQUESTS_EXCEPTION:
	print('Error')

else:
	print('${}'.format(response.json()['data']['amount']))
