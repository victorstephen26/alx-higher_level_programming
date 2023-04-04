#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_division(matrix, div):
    """Thsi function divides all elements of amatrix by a given number
    Args:
        matrix: A list of lists (matrix) can be of type ints or float
        div: Number to bbe used for the division (can be a  float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of differnt sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Rturns:
        A new matrix which represents the result of the divisions
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix mst have same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise ZeroDivisionError("division by zero")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])