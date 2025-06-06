#!/usr/bin/python3
"""
This module allow the function
"""


def write_file(filename="", text=""):
    """
    function that writes a string
    """
    with open(filename, 'w', encoding='utf-8') as f:
        nb = f.write(text)
        return nb
