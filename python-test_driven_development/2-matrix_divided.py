#!/usr/bin/python3
"""
This module test function who divide all elements of matrix
"""


def matrix_divided(matrix, div):
    """
    Function divide elements of matrix
    """
    for row in matrix:
        for i in row:
            if not isinstance(i, float) and not isinstance(i, int):
                raise TypeError(
                    "matrix must be a matrix"
                    " (list of lists) of integers/floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
