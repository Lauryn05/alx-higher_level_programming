#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): Number of rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height"""
        return self.__height = value
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
            """Return area"""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return perimeter"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))

        def __str__(self):
            """Return printable rep of the rectangle

            Rep rectangle with #
            """
            if self.__width == 0 or self.__height == 0:
                return ("")

            draw = []
            for a in range(self.__height):
                [draw.append('#') for b in range(self.__width)]
                if a != self.__height - 1:
                    draw.append("\n")
            return ("".join(draw))

        def __repr__(self):
            """Return string rep of rectangle"""
            draw = "Rectangle(" + str(self.__width)
            draw = draw + ", " + str(self.__height) + ")"
            return (draw)

        def __del__(self):
            """Print message for every deletion of rectangle"""
            type(self). number_of_instances -= 1
            print("Bye rectangle...")
