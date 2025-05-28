#!/usr/bin/python3
"""
check if the object is an instance of a class that inherited specified class
"""


def inherits_from(obj, a_class):
    """
    the object and the class
    """

    if type(obj) is a_class:
        """
        condition that check if True or False
        """

        return False
    else:
        return isinstance(obj, a_class)
