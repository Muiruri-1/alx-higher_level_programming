#!/usr/bin/python3
def raise_exception():
    try:
        # Raise a custom type exception
        raise TypeError("This is a custom type exception")
    except TypeError as e:
        # Handle the exception and print a custom message
        print(e)
