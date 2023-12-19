#!/usr/bin/python3

"""
    Prints an integer using "{:d}".format().

    Args:
        Value to print.

    Returns:
        True if the value is an integer, otherwise False.
"""


def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except (Exception) as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return (False)
