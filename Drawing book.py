#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    count_front = int()
    count_end = int()
    if p == 1 or n == p or (n % 2 != 0 and p == n - 1):
        return 0
    else:
        page = p
        if p % 2 != 0:
            page = p - 1
        count_front = int(page / 2)
    if True:
        no = n
        diff = no - p
        if diff == 1:
            count_end = diff
        else:
            count_end = int(diff / 2)
    print(count_front, count_end)
    if count_front < count_end:
        return count_front
    else:
        return count_end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
