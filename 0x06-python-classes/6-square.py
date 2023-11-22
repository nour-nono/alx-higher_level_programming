#!/usr/bin/python3
""" this is square module, and it is the first in oop """


class Square:
    """ this is square class"""
    def __init__(self, size=0, position=(0, 0)):
        """ this is the constructor
            Args:
                size: The first parameter.
                position: square position in x-axis and y-axis
            Raises:
                TypeError: If size is not an integer
                or position is not a tuple of 2 positive integers.
                ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ property size is the size of each side of the square

           Returns:
               the size of the square.
           """
        return self.__position

    @position.setter
    def position(self, value):
        """ methode size is a setter for size attribute
            Args:
                value: size value.
        """
        if (type(value) is not tuple or len(value) != 2
            or type(value[0]) is not int or type(value) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ methode my_print prints in stdout the square with the character #
        """
        for y in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
