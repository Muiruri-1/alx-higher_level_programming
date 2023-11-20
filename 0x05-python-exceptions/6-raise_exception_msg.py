#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        # Raise a custom name exception with the provided message
        raise NameError(message)
    except NameError as e:
        # Handle the exception and print the custom message
        print(e)
