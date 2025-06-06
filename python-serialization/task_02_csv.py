#!/usr/bin/env python3
"""Saves some CSV data into JSON file"""
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
