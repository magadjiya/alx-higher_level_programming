#!/usr/bin/python3

"""
This module defines a square with a private attr size

Class:
    Square: A square with private size
"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Initializes a Square instance with private attribute size

        Args:
            @size (int): The size of the square, default value is 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is a negative value
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)
