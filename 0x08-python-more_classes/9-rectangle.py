#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        print_symbol (any): Symbol used for string rep
        number_of_instances (int): Number of rectangle instances
    """
    
    print_symbol = "#"
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

     @staticmethod
     def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

        def area(self):
            """Return area"""
            return (self.__width * self.__height)

        def perimeter(self):
            """Return perimeter"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))

        @classmethod
        def square(cls, size=0):
            """Return a new rectangle with width and height equal to size

            Args:
                size (int): width and height of new rectangle
            """
            return (cls(size, size))

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
