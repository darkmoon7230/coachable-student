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
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self._cum = []
        acc = 0
        for ele in w:
            acc += ele
            self._cum.append(acc)
        self._sum = acc

    def pickIndex(self) -> int:
        val = random.randint(1, self._sum)
        idx = bisect.bisect_left(self._cum, val)
        return idx

