#!/usr/bin/env python3
"""
Module 0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise

    Parameters
    ---------
    matrix: list[list[int]]
        2d matrix
    """
    copy_matrix = [row[:] for row in matrix]
    for i in range(0, 3):
        for j in range(2, -1, -1):
            matrix[j][2-i] = copy_matrix[i][j]
