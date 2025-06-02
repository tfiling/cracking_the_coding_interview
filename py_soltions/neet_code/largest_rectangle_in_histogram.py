# https://neetcode.io/problems/largest-rectangle-in-histogram
from typing import List

from py_soltions.useful_ds.stack import Stack


def largest_rectangle_in_histogram_v1_not_working(heights: List[int]) -> int:
    res = 0
    stack = Stack()
    for i in range(len(heights)):
        if len(stack) == 0:
            stack.push((i, heights[i]))
            continue
        idx, height = stack.peek()
        if height <= heights[i]:
            stack.push((i, heights[i]))
            continue
        while height > heights[i]:
            stack.pop()
            curr_rec_size = ((i + 1) - idx) * height
            res = max(res, curr_rec_size)
            if len(stack) == 0:
                break
            idx, height = stack.peek()
        stack.push((idx, heights[i]))
    i = len(heights)
    while len(stack) > 0:
        idx, height = stack.pop()
        curr_rec_size = ((i + 1) - idx) * height
        res = max(res, curr_rec_size)
    return res

def largest_rectangle_in_histogram(heights: List[int]) -> int:
    res = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            res = max(res, height * (i - index))
            start = index
        stack.append((start, h))
    for start, h in stack:
        res = max(res, h * (len(heights) - start))
    return res


if __name__ == '__main__':
    print(f"{largest_rectangle_in_histogram([2,1,5,6,2,3])} ?? 10")