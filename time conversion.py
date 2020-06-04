#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    result=""
    if s[8] == 'p' or s[8] == "P":
        s=s[:8]
        arr=s.split(':')
        ar =int(arr[0])
        if ar==12:
          pass
        else:
            ar=ar+12
        arr[0]=str(ar)
        arr=":".join(arr)
        result=arr
    else:
        s=s[:8]
        arr=s.split(':')
        ar =int(arr[0])
        if ar==12:
          arr[0] ='00'
        arr=":".join(arr)
        result=arr
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
