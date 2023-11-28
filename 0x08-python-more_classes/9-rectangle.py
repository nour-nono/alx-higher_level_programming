#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The symbol used to represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The constructor for the Rectangle class.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            If either the width or height is 0, the perimeter is also 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the bigger area.

        Parameters:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """
        Return a string representation of the rectangle.

        The rectangle is represented as a string of '#' characters,
        with one '#' character for each unit of width and height.
        If either the width or height is 0,
        an empty string is returned.

        Returns:
            str: A string representation of the rectangle.
        """
        s = ""
        if self.height == 0 or self.width == 0:
            return s
        for x in range(self.height):
            for y in range(self.width):
                s += str(self.print_symbol)
            if x != (self.height - 1):
                s += "\n"
        return s

    def __repr__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object
            in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Perform cleanup operations when the Rectangle object is deleted.

        This method prints a message indicating
        that the rectangle is being deleted and
        decreases the number of instances.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """
        Create a square Rectangle.

        Parameters:
            size (int): The size of the square.

        Returns:
            Rectangle: A square Rectangle with the given size.
        """
        return cls(size, size)
