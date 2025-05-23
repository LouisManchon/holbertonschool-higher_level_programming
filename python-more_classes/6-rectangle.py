#!/usr/bin/python3
"""
0-rectangle.py
Write an class Rectangle that define a rectangle
"""


class Rectangle:
    """
    Create a class Rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        def the arguments and conditions of initialisation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)

        return "\n".join(lines)

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

    def area(self):
        """
        Return the area of the rectangle
        """
        rectangle_area = self.width * self.height
        return rectangle_area

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        """
        perimeter_rectangle = 0
        if self.width == 0 or self.height == 0:
            perimeter_rectangle = 0
        else:
            perimeter_rectangle = ((self.height + self.width) * 2)
        return perimeter_rectangle

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
