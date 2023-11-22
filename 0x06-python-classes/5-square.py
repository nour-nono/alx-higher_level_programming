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
        self.size = size

    def area(self):
        """methode area to compute the area of the square

           Returns:
               the area of the square.
           """
        return self.__size ** 2

    @property
    def size(self):
        """ property size is the size of each side of the square

           Returns:
               the size of the square.
           """
        return self.__size

    @size.setter
    def size(self, value):
        """ methode size is a setter for size attribute
            Args:
                value: size value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ methode my_print prints in stdout the square with the character #
        """
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
