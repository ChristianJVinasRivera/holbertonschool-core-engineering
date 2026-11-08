#!/usr/bin/env python3
"""Find the key with the highest integer value."""


def best_score(a_dictionary):
    """Return the highest-scoring key, or None for an empty input."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
