import time
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            
        # return [list(three) for three in res]


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    print(s.threeSum([0] * 3000))
    print(f"took {time.time() - start} seconds")

    def my_sol_too_slow(self, nums: List[int]) -> List[List[int]]:
        res = set()
        numbers_mapping = {}
        for num, idx in zip(nums, range(len(nums))):
            curr_dups = numbers_mapping.get(num, set())
            if len(curr_dups) < 3:
                curr_dups.add(idx)
                numbers_mapping[num] = curr_dups
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                expected_third = (nums[i] + nums[j]) * -1  # should sum to 0
                if expected_third in numbers_mapping:
                    third_candidates = set(numbers_mapping[expected_third])
                    third_candidates -= {i, j}
                    if third_candidates:
                        res.add(tuple(sorted([nums[i], nums[j], expected_third])))
        return [list(three) for three in res]
