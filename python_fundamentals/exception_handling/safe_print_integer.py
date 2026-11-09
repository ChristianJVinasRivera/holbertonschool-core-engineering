#!/usr/bin/env python3
"""Print an integer safely."""


def safe_print_integer(value):
    """Print an integer and return whether printing succeeded."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
