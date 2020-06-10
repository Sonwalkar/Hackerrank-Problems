#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.

"""
def formingMagicSquare(mat: list) -> int:
    cost_list = [sys.maxsize] * len(matrix_list)
    for ref_mat in matrix_list:
        cost = 0
        for x in range(0, len(mat)):
            for y in range(0, len(mat)):
                if mat[x][y] != ref_mat[x][y]:
                    cost += abs(mat[x][y] - ref_mat[x][y])
        cost_list.append(cost)
    return min(cost_list)
"""

def formingMagicSquare(s):
    matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                   [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                   [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                   [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                   [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                   [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                   [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                   [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    for i in matrix_list:
        if s in matrix_list:
            print("Yes")
        else:
            for k in range(3):
                for j in range(3):
                    if s[k][j] !=  i[k][j]:
                        print(abs(s[k][j] - matrix_list[k][j]))
        print(matrix_list[i])

if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    formingMagicSquare(s)

