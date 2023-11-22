#!/usr/bin/python3
""" this is square module, and it is the first in oop """


class Square:
    """ this is square class"""
    def __init__(self, size=0):
        """ this is the constructor
            Args:
                size: The first parameter.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """methode area to compute the area of the square

           Returns:
               the area of the square.

           """
        return self.__size ** 2
