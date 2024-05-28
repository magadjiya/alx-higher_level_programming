#!/usr/bin/python3

"""
This module defines a square with a private
attribute size

Class:
    Square: a square with a private size
"""


class Square:
    """Defines a square based on 0-square.py"""

    def __init__(self, size):
        """
        Initializes the square instance with a private size

        Args:
            @size (int):  The size of the square
        """
        self.__size = size
