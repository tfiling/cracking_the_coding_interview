from typing import List

# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        i = 0
        j = len(height) - 1
        while i < j:
            curr_volume = (j - i) * min([height[i], height[j]])
            curr_max = max(curr_max, curr_volume)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return curr_max

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,2,4,3]))