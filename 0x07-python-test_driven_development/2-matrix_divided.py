#!/usr/bin/python3
"""Module for matrix_divided method."""

def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    returns:
        list: List of lists representing divided matrix.
    raises:
        TypeError: if matrix is not list of lists containing int or float.
        TypeError: if sublists are not all same size.
        TypeError: if div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for f in r:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(f / div, 2) for f in r] for r in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
