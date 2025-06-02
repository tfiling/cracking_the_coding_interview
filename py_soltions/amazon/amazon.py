#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    arr.sort(reverse=True)
    b_sum = sum(arr)
    a_sum = 0
    a = []
    for num in arr:
        b_sum -= num
        a_sum += num
        a.append(num)
        if a_sum > b_sum:
            break
    return sorted(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
