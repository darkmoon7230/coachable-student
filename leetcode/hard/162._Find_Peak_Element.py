# Link to problem: https://leetcode.com/problems/find-peak-element/description/
# Loom explaining solution you wrote (5m):
# Solution:
# Description
# Key ideas
# TODO
# Difficulty: Hard
# Code

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        up = len(nums) - 1
        while lo != up:
            mid_i = lo + (up - lo) // 2
            mid_v = nums[mid_i]
            mid_next_v = nums[mid_i + 1]
            if mid_next_v > mid_v:  # increasing, must be on the right
                lo = mid_i + 1
            else:  # decreasing
                # we might be at peak
                if mid_i == 0 or nums[mid_i - 1] < mid_v:
                    return mid_i
                # search left part
                up = mid_i - 1
        return lo


