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

import heapq


class CustomHeap:
    def __init__(self):
        # Initialize empty heap
        self._heap = []

    def push(self, item):
        """
        Push a 3-tuple onto the heap.
        The tuples are ordered by the difference of first two elements (in descending order).

        Args:
            item (tuple): A 3-tuple of integers (a, b, c)
        """
        if not isinstance(item, tuple) or len(item) != 3:
            raise ValueError("Item must be a 3-tuple")

        # Multiply by -1 to get max heap (descending order) instead of min heap
        priority = -(item[0] - item[1])
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        """
        Remove and return the 3-tuple with the largest difference between first two elements.

        Returns:
            tuple: A 3-tuple of integers (a, b, c)

        Raises:
            IndexError: If heap is empty
        """
        if not self._heap:
            raise IndexError("pop from empty heap")

        return heapq.heappop(self._heap)[1]

    def peek(self):
        """
        Return the 3-tuple with the largest difference between first two elements without removing it.

        Returns:
            tuple: A 3-tuple of integers (a, b, c)

        Raises:
            IndexError: If heap is empty
        """
        if not self._heap:
            raise IndexError("peek from empty heap")

        return self._heap[0][1]

    def __len__(self):
        """Return the number of items in the heap."""
        return len(self._heap)

    def __bool__(self):
        """Return True if heap has items, False otherwise."""
        return bool(self._heap)



def _count_items(s, start_idx, end_idx):
    res = 0
    for i in range(start_idx, end_idx + 1):
        if s[i] == "*":
            res += 1
    return res


def _find_compartments(s, start_idx, end_idx, res_cache: CustomHeap, curr_depth):
    # start_idx, end_idx are inclusive, 0 based
    if not s:
        return 0, -1, -1
    res = 0
    while start_idx < end_idx and s[start_idx] != "|":
        start_idx += 1
    while end_idx > start_idx and s[end_idx] != "|":
        end_idx -= 1
    if start_idx < end_idx:
        if curr_depth < 500:
            for _, (cache_res_start, cache_res_end, cached_item_count) in res_cache._heap:
                if start_idx <= cache_res_start and end_idx >= cache_res_end:
                    return (cached_item_count +
                            _find_compartments(s, start_idx, cache_res_start, res_cache, curr_depth+1)[0] +
                            _find_compartments(s, cache_res_end, end_idx, res_cache, curr_depth+1)[0]), start_idx, end_idx
        # Cache miss or too deep recursion
        res = _count_items(s, start_idx, end_idx)
    return res, start_idx, end_idx


def numberOfItems(s, startIndices, endIndices):
    res = []
    res_cache = CustomHeap()
    for i in range(len(startIndices)):
        items_count, compartment_start, compartment_end = _find_compartments(s, startIndices[i] - 1, endIndices[i] - 1, res_cache, 0)
        if compartment_start > 0 and compartment_end > 0:
            # Valid cache res
            res_cache.push((compartment_start, compartment_end, items_count))
        res.append(items_count)
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
