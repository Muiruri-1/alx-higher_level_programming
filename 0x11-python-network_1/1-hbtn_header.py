#!/usr/bin/python3
"""
The script takes a URL, sends request, and displays the X-Request-Id variable
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
