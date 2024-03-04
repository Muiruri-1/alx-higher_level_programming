#!/bin/bash
# This script displays the body of a successful GET request response (200 code)
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep 200 && curl -s "$1"
