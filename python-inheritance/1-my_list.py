#!/usr/bin/python3
"""
This module print the list but sorted ascending sort
"""
class MyList(list):
    """
    That's my list
    """

    def print_sorted(self):
        """
        Print a list sorted
        """
        copy = self[:]
        copy.sort()
        print(copy)
