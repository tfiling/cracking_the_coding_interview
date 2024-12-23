#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def _count_items(s, start_idx, end_idx):
    # start_idx, end_idx are inclusive, 0 based
    if not s:
        return 0
    res = 0
    while start_idx < end_idx and s[start_idx] != "|":
        start_idx += 1
    while end_idx > start_idx and s[end_idx] != "|":
        end_idx -= 1
    if start_idx < end_idx:
        for i in range(start_idx, end_idx+1):
            if s[i] == "*":
                res += 1
    return res


def numberOfItems(s, startIndices, endIndices):
    res = []
    for i in range(len(startIndices)):
        res.append(_count_items(s, startIndices[i] - 1, endIndices[i] - 1))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
