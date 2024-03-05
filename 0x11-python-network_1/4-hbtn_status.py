#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using requests package
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    data = response.text

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
