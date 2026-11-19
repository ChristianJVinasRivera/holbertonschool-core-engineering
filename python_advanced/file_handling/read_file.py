#!/usr/bin/env python3
"""Read a UTF-8 text file."""


def read_file(filename=""):
    """Print the contents of a text file to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
