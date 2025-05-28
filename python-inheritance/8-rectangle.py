#!/usr/bin/python3
"""
This module is just a class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initializes a rectangle with width and height
    """

    def __init__(self, width, height):
        """
        init a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
