#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Returns a new matrix with all elements divided by div.

        Parameter:
            matrix (list): The matrix to be divided.
            div (int or float): The number to divide by.

        Raises:
            TypeError: If matrix is not a list of lists of int/floats,
                       If each row of the matrix does not have the same size.
            ZeroDivisionError: if div is 0.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not all(isinstance(item, (int, float)) \
for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([[round(item / div, 2) for item in row] for row in matrix])
