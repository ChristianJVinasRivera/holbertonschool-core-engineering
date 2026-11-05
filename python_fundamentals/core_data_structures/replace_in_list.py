#!/usr/bin/env python3
"""Replace a list element at a valid index."""


def replace_in_list(my_list, idx, element):
    """Return the original list after replacing a valid position."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
