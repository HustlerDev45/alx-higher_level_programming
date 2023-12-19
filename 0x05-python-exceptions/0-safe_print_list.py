#!/usr/bin/python3

"""
    Prints the first x elements of a list and only integers.

    Returns:
        int: Real number of elements printed.
"""

def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            n += 1
        except IndexError:
            break
        print()
        return (n)
