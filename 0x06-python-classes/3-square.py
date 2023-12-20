#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Define a Square."""

    def __init__(self, size=0):
        """
            Define a new Square.

            Parameters:
                size (int): New Square's size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns Square area."""
        return self.__size ** 2
