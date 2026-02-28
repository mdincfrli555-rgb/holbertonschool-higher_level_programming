#!/usr/bin/python3
"""This module defines a class Square that represents a geometric square."""

class Square:
    """A class used to represent a Square with a private inistance attibute."""

    def __init__(self, size):
        """Initializes a new inistance of the Square class.

        Args:
            size (int): The side of the square.
        """
        self.__size = size
