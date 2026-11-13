#!/usr/bin/env python3
"""Define a square with its own string representation."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a validated square with a specialized description."""

    def __str__(self):
        """Return the square description and its equal dimensions."""
        return super().__str__().replace('[Rectangle]', '[Square]', 1)
