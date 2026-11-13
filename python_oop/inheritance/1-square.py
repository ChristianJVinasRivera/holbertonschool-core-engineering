#!/usr/bin/env python3
"""Define a square using the rectangle's geometry behavior."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a validated private size."""

    def __init__(self, size):
        """Validate size and initialize equal rectangle dimensions."""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square of the side length."""
        return self.__size ** 2
