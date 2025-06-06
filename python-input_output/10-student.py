#!/usr/bin/python3
"""
8-student.py
write a class Student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__

            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
        else:
            return self.__dict__
