#!/usr/bin/python3

"""
    Prints an int with "{:d}".format().

    Args:
        value: Value to print (might be any type).

    Returns:
        bool: True if ValueError, otherwise False.
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
