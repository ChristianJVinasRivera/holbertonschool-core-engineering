#!/usr/bin/env python3
"""Define a square with a private size attribute."""


class Square:
    """Represent a square with a size."""

    def __init__(self, size):
        """Initialize the square with the given size."""
        self.__size = size
