#!/usr/bin/python3
"""Serializes and deserializes data from a filename"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it in a json file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes a dictionary from a json file"""
    with open(filename, 'r+', encoding="utf-8") as f:
        return json.load(f)
