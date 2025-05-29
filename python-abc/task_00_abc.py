#!/usr/bin/python3
from abc import ABC, abstractmethod

"""
This module have abstract class and subclass
"""


class Animal(ABC):
    """
    Abstract class allow subclasses generique methodes
    """

    @abstractmethod
    def sound(self):
        """
        Methods for all subclass
        """
        pass


class Dog(Animal):
    """
    Class of dog
    """

    def sound(self):
        """
        Sound of the dogs
        """
        return "Bark"


class Cat(Animal):
    """
    Class of cat
    """

    def sound(self):
        """
        Sound of the cats
        """
        return "Meow"
