#!/bin/bash
# This script takes a URL as input and displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
