#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Define a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
            Define a new Square.

            Parameters:
                size (int): New Square's size.
                position: New Square's position.
        """
        self.size = size
        self.position = position

    @property
    def size(size):
        """Gets Square's size."""
        return self.__size

    @size.setter
    def size(size, value):
        """Sets Square's size."""
        if not isinstance(value, int):
            raise TypeError("size mist be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets Square's position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets Square's position."""
        if not isinstance(value, tuple) or len(value) != 2 or
        not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """Returns Square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints Square with # character."""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
