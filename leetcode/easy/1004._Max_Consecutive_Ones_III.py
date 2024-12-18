# Link to problem: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1438277116/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# This is a classic sliding window problem
# Difficulty: Easy
# Code

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lo, up = 0, 0
        longest, current, current_k = 0, 0, k
        while up != len(nums):
            # we can grow trivially
            if nums[up] == 1:
                up += 1
                current += 1
            else:
                # we can use corrections
                if current_k > 0:
                    current_k -= 1
                    up += 1
                    current += 1
                else:  # we run out of corrections
                    if nums[lo] == 0:  # steal correction from front
                        lo += 1
                        up += 1
                    else:  # shrink
                        lo += 1
                        current -= 1
            longest = max(longest, current)
        return longest

