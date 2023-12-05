#!/usr/bin/python3
"""
This module provides a function for read a text from file.
"""


def read_file(filename=""):
    """
    Reads the content of a specified file and prints it.

    Parameters:
        filename (str): The name of the file to read from.

    Returns:
        None
    """
    with open(filename, "r") as fl:
        print(fl.read(), end="")
