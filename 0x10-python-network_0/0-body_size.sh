#!/bin/bash

# Check if a URL argument is provided
if [-z "$1"]; then
	echo "Error: Please provide a URL as an argument."
	exit 1
fi

# URL from the first argument
url="$1"

# Get the response header only with the -sI option and pipe it to grep for Content-Length
size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')

# Check if size is empty (not found in header)
if [ -z "$size" ]; then
	echo "Error: Content-Length not found in response header."
else
	echo "Response size for $url: $size bytes"
fi
