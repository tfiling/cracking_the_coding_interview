from typing import List
import time
import statistics


# https://leetcode.com/problems/3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return [list(three) for three in res]


def measure_performance(func, *args, iterations=100):
    execution_times = []

    for _ in range(iterations):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        execution_times.append(end_time - start_time)

    avg_time = statistics.mean(execution_times)
    min_time = min(execution_times)
    max_time = max(execution_times)

    print(f"Function: {func.__name__}")
    print(f"Average execution time: {avg_time:.8f} seconds")
    print(f"Minimum execution time: {min_time:.8f} seconds")
    print(f"Maximum execution time: {max_time:.8f} seconds")
    print(f"Standard deviation: {statistics.stdev(execution_times):.8f} seconds")



if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    # print("their sol:")
    # measure_performance(s.threeSum, [-1,0,1,2,-1,-4], iterations=100000)
    # print("my sol:")
    # measure_performance(s.threeSum2, [-1,0,1,2,-1,-4], iterations=100000)

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
