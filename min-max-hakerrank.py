#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, a):
    a.sort()
    k -= 1
    mini = 1000000
    # for i in range(len(a)-k+1):
    #     s = a[i:i+k][k-1] - a[i:i+k][0]
    #     if s <= mini:
    #         mini = s
    # return(mini)f
    return min(a[i+k]-a[i] for i in range(len(a)-k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()