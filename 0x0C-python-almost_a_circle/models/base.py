#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Base class for other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the object.

        Args:
            id (int, optional): The id of the object.
        """
        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
