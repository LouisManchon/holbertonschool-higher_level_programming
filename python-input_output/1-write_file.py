#!/usr/bin/python3
"""
This module allow the function
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, 'r', encoding='utf-8')as f:
        print(f.write(), end="")
