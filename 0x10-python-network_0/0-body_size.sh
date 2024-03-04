#!/bin/bash
# This script takes a URL as input, sends a request using curl and displays the size in bytes
curl -sI "$1" | grep -i content-length | awk '{print $2}'

