#!/usr/bin/env python3
"""Compute powers using repeated multiplication."""


def pow(a, b):
    """Return a raised to the integer power b."""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
