#!/usr/bin/python3

"""
This module contains a class Rectangle

Class:
    Rectangle: a class
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with width and height

        Args:
            @width (int): the rectangle's width
            @height (int): the rectangle's height

        Raises:
            TypeError: If width/height is not an integer
            ValueError: If width/height is less than or equal to zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
