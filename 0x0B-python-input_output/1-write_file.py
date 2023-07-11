#!/usr/bin/python3
"""Defines file writing function"""


def write_file(filename="", text=""):
    """Write a string to UTF8 text file

    Args:
        filename (str): Name of file to write
        text (str): text written to the file
    Returns:
        Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
