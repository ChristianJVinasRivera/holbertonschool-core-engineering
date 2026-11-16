#!/usr/bin/env python3
"""Abstract shapes and a duck-typed information function."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Define the interface shared by geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle using its radius."""

    def __init__(self, radius):
        """Initialize the radius."""
        self.radius = radius

    def area(self):
        """Return pi times the radius squared."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circumference."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle using its width and height."""

    def __init__(self, width, height):
        """Initialize the dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Return the product of the dimensions."""
        return self.width * self.height

    def perimeter(self):
        """Return twice the sum of the dimensions."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter without checking the object's type."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
