#!/usr/bin/env python3
"""Helpers for working with numeric digits."""


def print_last_digit(number):
    """Print and return the positive last digit of number."""
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
