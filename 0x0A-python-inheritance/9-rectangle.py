#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize new Rectangle

        Args:
            width (int): Width of the new Rectangle
            height (int): Height of the new Rectangle
    """
    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height", height)
    self.__height = height

    def area(self):
        """Return Resctangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() rep of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
