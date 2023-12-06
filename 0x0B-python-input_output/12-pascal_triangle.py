#!/usr/bin/python3
"""
This module provide a func Generates Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows for which Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    ans = []
    for x in range(n):
        z = [1]
        for y in range(x):
            if y+1 >= x:
                z.append(1)
            else:
                z.append(ans[x-1][y]+ans[x-1][y+1])
        ans.append(z)
    return ans
