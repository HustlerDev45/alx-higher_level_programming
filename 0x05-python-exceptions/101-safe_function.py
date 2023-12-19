#!/usr/bin/python3

"""
    Safely executes a function.

    Returns:
        Result of the function, otherwise None.
"""


import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (Exception) as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return (None)
