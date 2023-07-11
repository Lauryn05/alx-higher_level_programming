#!/usr/bin/python3
"""Defines file appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file

    Args:
       filename (str): name of file to append to
       text (str): String to append to the file
    Returns:
       Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
