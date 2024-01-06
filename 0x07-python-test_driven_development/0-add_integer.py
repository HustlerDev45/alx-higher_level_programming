#!/usr/bin/python3
"""Addition of two integers."""


def add_integer(a, b=98):
    """Returns the addition of a and b.

        Args:
            a (int or float): First number.
            b (int or float): Second number.

        Returns: The sum of a and b.

        Raises:
            TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
