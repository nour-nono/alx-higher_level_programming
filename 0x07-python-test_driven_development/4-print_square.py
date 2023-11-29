#!/usr/bin/python3
"""
This module defines a function to print a square of a given size
filled with "#" characters.
"""


def print_square(size):
    """
    Prints a square of a given size, filled with "#" characters.

    Args:
        size: size of the square.
        It must be an integer and greater than or equal to 0.

    Raises:
        TypeError:If the size is not an integer.
        ValueError:If the size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
