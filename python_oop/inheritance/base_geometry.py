#!/usr/bin/env python3
"""Define shared behavior and validation for geometric shapes."""


class BaseGeometry:
    """Provide a geometry interface and positive integer validation."""

    def area(self):
        """Signal that subclasses must implement the area calculation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a named value is an integer greater than zero."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
