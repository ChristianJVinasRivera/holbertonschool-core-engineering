#!/usr/bin/env python3
"""Write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Return the number of characters written to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
