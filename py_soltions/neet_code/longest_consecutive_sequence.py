# https://neetcode.io/problems/longest-consecutive-sequence
from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    res = 0
    curr_sequence_len = 1
    nums_set = set(nums)
    for num in nums:
        if num not in nums_set:
            # Already processed
            continue
        offset = 1
        while num + offset in nums_set:
            # Scan sequence to the right
            curr_sequence_len += 1
            nums_set.remove(num + offset)
            offset += 1
        offset = 1
        while num - offset in nums_set:
            # Scan sequence to the left
            curr_sequence_len += 1
            nums_set.remove(num - offset)
            offset += 1
        res = max(curr_sequence_len, res)
    return res
