#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not is instance(value, tuple) or
                not all(isinstance(num, int)for num on value) or
                len(value) != 2 or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be in tuple of 2 positive integers")
        self.position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for a in range(0, self.__position[1])]
        for b in range(0, self.__size):
            [print(" ", end="") for c in range(0, self.__position[0])]
            [print("#", end="") for d in range(0, self.__size)]
            print("")
