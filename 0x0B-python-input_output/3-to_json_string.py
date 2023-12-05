#!/usr/bin/python3
"""
This module provides a function converts a Python object into a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object into a JSON string.

    This function convert a Python object into a JSON string.

    Args:
        my_obj (object): The Python object to be converted.

    Returns:
        str: The JSON string representation of the input object.

    Raises:
        TypeError: If the input object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
