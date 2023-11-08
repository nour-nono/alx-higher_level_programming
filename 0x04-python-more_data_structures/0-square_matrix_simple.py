#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    if matrix is None:
        return
    for x in matrix:
        a.append([pow(y, 2) for y in x])
    return a
