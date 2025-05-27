#!/usr/bin/python3
"""
check if the object is an instance of a class or class that inherited from
"""
def is_kind_of_class(obj, a_class):
    """
    the obj and the class
    """
    if isinstance(obj, a_class):
        """
        check if True or False
        """
        return True
    else:
        return False
