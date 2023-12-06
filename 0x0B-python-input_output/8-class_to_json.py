#!/usr/bin/python3
"""
This module Convert a Python object into a dictionary.
"""


def class_to_json(obj):
    """
    Convert a Python object into a dictionary.

    Args:
        obj (object): The Python object to be converted.

    Returns:
        dict: A dictionary representation of the input object.
    """
    ans = {}
    for x in dir(obj):
        if not x.startswith("__"):
            ans[x] = obj.__getattribute__(x)
    return ans
