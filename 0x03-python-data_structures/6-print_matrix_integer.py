#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for c in mat:
            print("{:d}".format(c), end=" " if c != mat[-1] else "")
        print()
