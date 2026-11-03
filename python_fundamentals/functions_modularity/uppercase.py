#!/usr/bin/env python3
"""ASCII uppercase conversion."""


def uppercase(str):
    """Print str in uppercase, followed by a newline."""
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
