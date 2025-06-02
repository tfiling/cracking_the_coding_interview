# https://neetcode.io/problems/top-k-elements-in-list
from typing import List


class Solution:
    def topKFrequent_nlogn(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = {}
        for num in nums:
            frequency_counter[num] = frequency_counter.get(num, 0) + 1
        freq_lst = [(num, freq) for num, freq in frequency_counter.items()]
        freq_lst.sort(key=lambda x: x[1], reverse=True)
        return [num for (num, freq) in freq_lst[:k]]
