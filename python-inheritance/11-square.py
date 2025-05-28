#!/usr/bin/python3
"""
This module is just a class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        """
        Format a description of object
        """

        new_str = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return new_str
