# Link to problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# Loom explaining solution you wrote (5m): 
# Solution:
# Description:
# Find the value first, search for the end of the largest value on the left and the smallest value on the right.
# Key ideas
# Binary Search
# Difficulty: Easy

import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lhs = bisect.bisect_left(nums, target)

        if lhs == len(nums) or nums[lhs] != target:
            return [-1, -1]

        rhs = bisect.bisect_left(nums, target + 1)
        return [lhs, rhs - 1]

