#!/usr/bin/python3
"""
This module uses duck typing to create subclasses and adapted methods
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class defining a generic shape
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle shape class
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Displays area and perimeter of a shape using duck typing
    """
    print("Area: {:.2f}".format(shape.area()))
    print("Perimeter: {:.2f}".format(shape.perimeter()))
