# Link to problem:  https://leetcode.com/problems/random-pick-with-weight/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Generate a cumulative sum array
# Get a random number from 0 to sum of the weight array (exclusive)
# Binary search the number against the cumulative sum
# Difficulty:
# Medium (easier side of medium)
# Code


import random

def bisect_left(arr: List[int], target: int) -> int:
    lo, high = 0, len(arr)
    while lo < high:
        mid = lo + (high - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            high = mid
    return lo

class Solution:

    def __init__(self, w: List[int]):
        self._cumulative_weight = []
        self._total_weight = 0
        for ele in w:
            self._total_weight += ele
            self._cumulative_weight.append(self._total_weight)

    def pickIndex(self) -> int:
        val = random.randint(1, self._total_weight)
        idx = bisect_left(self._cumulative_weight, val)
        return idx

