#!/usr/bin/python3
""" add function module """


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int): The first integer to add.
    b (int): The second integer to add.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
