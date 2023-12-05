#!/usr/bin/python3
"""
This module provides a function converts a JSON string into a Python object
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string into a Python object.

    This function convert a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the input JSON string.
    """
    return json.loads(my_str)
