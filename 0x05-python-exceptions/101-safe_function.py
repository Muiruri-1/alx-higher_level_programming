#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Execute the provided function with the given arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Print the error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None

# Example usage:
# Define a sample function
def divide(a, b):
    return a / b
