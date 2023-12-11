#!/usr/bin/python3
"""
Rectangle class
"""
from base import Base


class Rectangle(Base):
    """
    A class rectangle with properties for width, height, and position.
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The id of the object.
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def y(self):
        """
        The y-coordinate of the rectangle's position.

        Returns:
           int: The y-coordinate of the rectangle's position.
        """
        return self.__width

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Parameters:
           value (int): The new y-coordinate of the rectangle's position.

        Raises:
           TypeError: If the y-coordinate is not an integer.
           ValueError: If the y-coordinate is less than 0.
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer or float")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value

    @property
    def x(self):
        """
        The x-coordinate of the rectangle's position.

        Returns:
           int: The x-coordinate of the rectangle's position.
        """
        return self.__width

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Parameters:
           value (int): The new x-coordinate of the rectangle's position.

        Raises:
           TypeError: If the x-coordinate is not an integer.
           ValueError: If the x-coordinate is less than 0.
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer or float")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__x = value

    @property
    def width(self):
        """
        The width of the rectangle.

        Returns:
           int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
           value (int): The new width of the rectangle.

        Raises:
           TypeError: If the width is not an integer.
           ValueError: If the width is less than 0.
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer or float")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The height of the rectangle.

        Returns:
           int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
           value (int): The new height of the rectangle.

        Raises:
           TypeError: If the height is not an integer.
           ValueError: If the height is less than 0.
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer or float")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
