#!/usr/bin/python3
"""
This module provides a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a given text to a specified file and returns the length of the text.

    Parameters:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The length of the written text.
    """
    with open(filename, "w") as fl:
        fl.write(text)
        return len(text)
