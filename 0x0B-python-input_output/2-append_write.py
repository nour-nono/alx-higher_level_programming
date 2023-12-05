#!/usr/bin/python3
"""
This module provides a function for appending a given text to a specified file.
"""


def append_write(filename="", text=""):
    """
    Writes a given text to a file and returns the length of text.

    Parameters:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The length of the written text.
    """
    with open(filename, "a") as fl:
        fl.write(text)
        return len(text)
