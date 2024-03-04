#!/bin/bash
# This script sends a JSON POST request to the URL provided and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
