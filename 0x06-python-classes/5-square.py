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
        self.size = size

    @property
    def size(self):
        """Gets Square's size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets Square's size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns Square area."""
        return(self.__size ** 2)

    def my_print(self):
        """Prints Square with # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
