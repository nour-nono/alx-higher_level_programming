#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


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
        return self.__y

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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """
        The x-coordinate of the rectangle's position.

        Returns:
           int: The x-coordinate of the rectangle's position.
        """
        return self.__x

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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        print a string representation of the rectangle.

        The rectangle is represented as a string of '#' characters,
         with one '#' character for each unit of width and height.
        """
        s = ""
        if self.height == 0 or self.width == 0:
            return s
        for x in range(self.height):
            for y in range(self.width):
                s += "#"
            if x != (self.height - 1):
                s += "\n"
        print(s)
