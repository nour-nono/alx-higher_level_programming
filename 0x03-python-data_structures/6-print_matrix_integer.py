#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    if len(matrix) == 0:
        print()
    else:
        for arr in (matrix):
            for ele in range(0, len(arr)):
                print("{:d}".format(arr[ele]), end="")
                if ele != len(arr)-1:
                    print(end=" ")
            print()
