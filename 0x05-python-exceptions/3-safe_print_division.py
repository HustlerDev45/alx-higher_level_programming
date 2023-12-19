#!/usr/bin/python3

"""
    Divide 2 integers and prints the result.

    Returns:
        The result of the division.
"""


def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except (ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
