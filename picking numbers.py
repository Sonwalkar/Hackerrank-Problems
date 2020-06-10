#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    maxcount = 0
    a.sort()
    for i in range(0 ,len(a)):
        currentcount = 1
        if i > 0:
            if a[i] == a[i-1]:
                print(a[i])
                continue
        for j in range(i+1, len(a)):
            if abs(a[j] - a[i]) <= 1:
                print(a[j], a[i])
                currentcount += 1
            else:
                break
        if currentcount > maxcount:
            maxcount = currentcount
    return maxcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
