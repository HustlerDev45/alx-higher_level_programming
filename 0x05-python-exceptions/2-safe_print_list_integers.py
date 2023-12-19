#!/usr/bin/python3

"""
    Prints 'x' elements of a list.

    Args:
        my_list (list): The list from elements should be printed.
        x (int): Number of elements of the list to print.

    Returns:
        int: Number of integers printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            continue
    print()
    return (n)
