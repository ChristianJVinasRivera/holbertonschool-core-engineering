#!/usr/bin/env python3
"""Add the first two elements of two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return two sums, treating missing values as zero."""
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return (a[0] + b[0], a[1] + b[1])
