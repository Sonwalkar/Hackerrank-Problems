#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    actual_charge = int((sum(bill) - bill[k])/2)
    if b == actual_charge:
        print("Bon Appetit")
    else:
        diff_of_charge = b - actual_charge
        print(diff_of_charge)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
