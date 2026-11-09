#!/usr/bin/env python3
"""Print integers from a list safely."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers in the first x positions and return their count."""
    count = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
