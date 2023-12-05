#!/usr/bin/python3
"""
module provides a func convert a Python obj into a JSON and save it to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Convert a Python object into a JSON string and save it to a file.

    This function convert a Python object into a JSON string.
    then writes the JSON string to a file specified by the filename parameter.

    Args:
        my_obj (object): The Python object to be converted.
        filename (str): The name of the file where the JSON will be saved.

    Returns:
        None
    """
    with open(filename, "w") as fl:
        fl.write(json.dumps(my_obj))
