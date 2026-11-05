#!/usr/bin/env python3
"""Print a matrix of integers row by row."""


def print_matrix_integer(matrix=[[]]):
    """Separate values with spaces and rows with newlines."""
    for row in matrix:
        for i, number in enumerate(row):
            if i > 0:
                print(" ", end="")
            print("{:d}".format(number), end="")
        print()
