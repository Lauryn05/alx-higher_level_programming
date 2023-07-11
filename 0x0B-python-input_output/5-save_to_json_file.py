#!/usr/bin/python3
"""Defines a string-to-JSON function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON rep"""
    with open(filename, "w") as f:
        json.dumps(my_obj, f)
