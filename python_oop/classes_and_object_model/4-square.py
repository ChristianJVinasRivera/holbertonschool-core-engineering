#!/usr/bin/env python3
"""Define a square with controlled access to its private size."""


class Square:
    """Represent a square with a non-negative integer size."""

    def __init__(self, size=0):
        """Initialize the square using the size property."""
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Validate and update the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
