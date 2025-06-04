#!/usr/bin/python3
"""
This module allow a reading files
"""


def read_file(filename=""):
    """
    Funtion to read a file
    """
    with open (filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
