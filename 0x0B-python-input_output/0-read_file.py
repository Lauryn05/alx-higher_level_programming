#!/usr/bin/python3
"""Definea a text-file-reading function"""


def read_file(filename=""):
    """Print the contenrs of a UTF8 text filr to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
