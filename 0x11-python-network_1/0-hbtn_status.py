#!/usr/bin/python3
"""
The script fetches status from https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data.decode("utf-8")))
