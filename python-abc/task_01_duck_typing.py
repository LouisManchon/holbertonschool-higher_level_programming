#!/usr/bin/python3
"""
This module use duck typing concept to create subclasses and adapted methods
"""


from abc import ABC, abstractmethod
import math

"""
This module have abstract class and subclass
"""


class Shape(ABC):
    """
    Abstract class allow subclasses generic methods
    """

    @abstractmethod
    def area(self):
        """
        Methods for all subclass
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Methods for all subclass
        """
        pass


class Circle(Shape):
    """
    Class of Circle
    """

    def __init__(self, radius):
        """
        Initialize the circle
        """
        self.__radius = radius

    def area(self):
        """
        Define area of the circle
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Define perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class of rectangle
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Define area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Define area of the rectangle
        """
        return 2 * (self.width + self.height)

    def shape_info(shape):
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
