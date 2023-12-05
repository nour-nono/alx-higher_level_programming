#!/usr/bin/python3
"""
This module defines a class `MyList`.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class.

    This function takes two arguments: an object and a class. It checks if the object is an instance of the class using the built-in Python function `isinstance()`. If the object is an instance of the class, the function returns `True`. Otherwise, it returns `False`.

    Parameters:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
    bool: `True` if the object is an instance of the class, `False` otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
