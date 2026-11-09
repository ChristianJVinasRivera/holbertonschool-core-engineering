#!/usr/bin/env python3
"""Print list elements safely."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements and return the number printed."""
    count = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
