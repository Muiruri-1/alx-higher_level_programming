#!/bin/bash
# This script takes a URL as input, sends a GET request using curl in silent mode, and displays the body of the response if the status code is 200
curl -s -o /tmp/response_body -w "%{http_code}" "$1" | awk '{ if ($0 == "200") { getline; print } }'
