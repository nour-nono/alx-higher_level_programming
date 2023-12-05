#!/usr/bin/python3
"""
This module defines a class `MyList`.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class.

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: `True` , `False`.
    """
    return type(obj) == a_class
