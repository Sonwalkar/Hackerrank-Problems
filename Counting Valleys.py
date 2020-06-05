#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    up = 0
    valley_count = 0
    for i in s:
        if sea_level <= 0:
            if i == 'U':
                sea_level += 1
            else:
                sea_level -= 1
            if sea_level == 0:
                valley_count += 1
        else:
            if i == 'U':
                sea_level += 1
            else:
                sea_level -= 1
        print(i,sea_level)
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
