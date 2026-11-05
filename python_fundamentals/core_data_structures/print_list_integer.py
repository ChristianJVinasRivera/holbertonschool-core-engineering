#!/usr/bin/env python3
"""Print each integer in a list on its own line."""


def print_list_integer(my_list=[]):
    """Print all list elements using integer formatting."""
    for number in my_list:
        print("{:d}".format(number))
