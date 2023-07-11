#!/usr/bin/python3
"""Defines a string-to-JSON function"""
import json


def from_json_string(my_str):
    """Return python obj of a JSON string"""
    return json.loads(my_str)
