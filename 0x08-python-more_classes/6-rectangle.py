#!/usr/bin/python3
"""Defines a class rectangle."""


class Rectangle:
    """Define the Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for n in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Returns the string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print (Bye rectangle) when an instance of rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
