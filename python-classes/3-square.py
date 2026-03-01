#!/usr/bin/python3
"""
This module defines the Square class for geometric calculations.
It provides functionality to initialize and calculate square areas.
"""

class Square:
    """
    A class used to represent a Square object.
    This class manages the size attribute and computes the area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with validation.

        Args:
            size (int): The side length of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the current area of the square.

        Returns:
            int: The area of the square (side squared).
        """
        return self.__size ** 2
