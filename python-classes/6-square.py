#!/usr/bin/python3
"""
This module Allow to learn POO with class
"""


class Square:
    """
    Define a class named Square
    """
    def __init__(self, size=0, position=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        symb = '#'

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
         return self.__size * self.__size 

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for symb in range(self.size):
                print('#' * self.size)
