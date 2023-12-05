#!/usr/bin/python3
"""
module provides a func Load a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    This function reads a JSON file specified by the filename parameter,
    and converts the JSON data into a Python object.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r") as fl:
        return json.load(fl)
