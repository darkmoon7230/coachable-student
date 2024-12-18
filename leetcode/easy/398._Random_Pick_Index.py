# Link to problem: https://leetcode.com/problems/random-pick-index/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Frequency map
# Difficulty: Easy
# Code

from random import choice

class Solution:

    def __init__(self, nums: List[int]):
        self.freq = dict()
        for i, num in enumerate(nums):
            if num not in self.freq:
                self.freq[num] = list()
            self.freq[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.freq[target])



