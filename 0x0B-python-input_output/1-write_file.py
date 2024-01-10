#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """
        Function that writes a string to a text file (UTF8)
        and returns the number of characters written.

        Returns:
            The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
