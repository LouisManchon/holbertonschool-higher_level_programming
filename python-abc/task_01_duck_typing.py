#!/usr/bin/python3
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
        """
        self.__radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
