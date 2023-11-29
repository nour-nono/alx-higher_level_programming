#!/usr/bin/python3
"""
This module defines a function to divide each element of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by a number.

    Args:
        matrix (list of list of int or float): The matrix to be divided.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of list of float: The matrix after division.
        Each element is rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If matrix doesn't have
            the same number of elements in each row.
        TypeError: If the div is not a number.
        ZeroDivisionError: If the div is zero.
        Exception: If an unexpected error occurs.
    """
    def wrong(zz):
        """
           Raise an exception based on the input argument.

           Args:
               zz (str): The argument to check.
               It should be one of "size", "type", "div_number", or "zero".

           Raises:
               TypeError: If the matrix is not a
               list of lists of int or floats.
               TypeError: If the matrix does not
               have the same number of elements in each row.
               TypeError: If the div is not a number.
               ZeroDivisionError: If the div is zero.
               Exception: If an unexpected error occurs.
        """
        if zz is None:
            return
        if zz == "size":
            raise TypeError("Each row of the matrix must have the same size")
        elif zz == "type":
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        elif zz == "div_number":
            raise TypeError("div must be a number")
        elif zz == "zero":
            raise ZeroDivisionError("division by zero")
        else:
            raise Exception("wrong argument")

    if not isinstance(div, int) and not isinstance(div, float):
        wrong("div_number")
    if div == 0:
        wrong("zero")
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        wrong("type")
    a = len(matrix[0])
    mm = []
    for x in matrix:
        if not isinstance(x, list):
            wrong("type")
        if len(x) != a:
            wrong("size")
        nn = []
        for y in x:
            if not isinstance(y, int) and not isinstance(y, float):
                wrong("type")
            y /= div
            nn.append(round(y, 2))
        mm.append(nn)
    return mm


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
