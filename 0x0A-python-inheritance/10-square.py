#!/usr/bin/python3
"""Defines a class Square that inherits from subclass Rectangle"""
Rectangle = __import__('9_rectangle').Rectangle


class Square(Rectangle):
    """Rep a Square"""

    def __init__(self, size):
        """Initialize new Square

        Args:
            size (int): Size of the new Square
    """
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size
