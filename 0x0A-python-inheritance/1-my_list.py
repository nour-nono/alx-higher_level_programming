#!/usr/bin/python3
"""
This module defines a class `MyList`.
"""


class MyList(list):
    """
    A class that extends the built-in Python `list` class.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method does not return anything. It directly prints the sorted
        elements of the list.
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
