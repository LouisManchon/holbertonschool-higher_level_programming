#!/usr/bin/python3
"""
0-rectangle.py
Write an class Rectangle that define a rectangle
"""


class Rectangle:
    """
    Create a class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        def the arguments and conditions of initialisation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        def the property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        def the setter width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        def the property height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        def the setter height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
