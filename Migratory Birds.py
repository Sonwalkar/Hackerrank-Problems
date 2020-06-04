#!/bin/python3
''' 'This algorithm takes too much time if length of array'
 typei = 0
    ln = len(arr)
    for i in arr:
        count = 0
        for j in range(ln):
            if i == arr[j]:
                count += 1
        if count > typei:
            typei = i
    return typei
    '''
import math
import os
import random
import re
import sys
# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    dict1 = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
    maximum = 0
    t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
    ln = len(arr)
    for i in arr:
        if i == 1:
            t1 += 1
            dict1[1] = t1
        elif i == 2:
            t2 += 1
            dict1[2] = t2
        elif i == 3:
            t3 += 1
            dict1[3] = t3
        elif i == 4:
            t4 += 1
            dict1[4] = t4
        elif i == 5:
            t5 += 1
            dict1[5] = t5
    maximum = max(dict1, key=dict1.get)
    return maximum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()