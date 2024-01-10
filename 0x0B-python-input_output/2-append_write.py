#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
        Function that appends a string at the end of a text file
        (UTF8) and returns the number of characters added.

        Returns:
            The numbers of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
