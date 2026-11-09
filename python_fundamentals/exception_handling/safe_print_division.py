#!/usr/bin/env python3
"""Divide two integers safely."""


def safe_print_division(a, b):
    """Print and return the division result, or None on failure."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
