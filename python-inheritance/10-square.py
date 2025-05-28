#!/usr/bin/python3
"""
This module is just a class
"""


class BaseGeometry:
    """
    This is the BaseGeometry class
    """

    def area(self):
        """
        Raises an Exception indicating that area is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        i

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Initializes a rectangle with width and height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    Initializes a square
    """

    def __init__(self, size):
        """
        Init square validator
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Define area
        """

        return self.__size * self.__size
