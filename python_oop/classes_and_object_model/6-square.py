#!/usr/bin/env python3
"""Define a square with a validated size and printing position."""


class Square:
    """Represent a square with a non-negative integer size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square using the size property."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the horizontal and vertical printing offsets."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and update the printing position."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(item, int) and item >= 0
                           for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square at its current position."""
        print(self)

    def __str__(self):
        """Return the positioned square without a trailing newline."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join(
            row for _ in range(self.__size))
