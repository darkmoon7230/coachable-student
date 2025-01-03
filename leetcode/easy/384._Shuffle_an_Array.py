# Link to problem: https://leetcode.com/problems/shuffle-an-array/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# random.shuffle is available
# This solution is obviously by construction.
# An iteration from front to back, swapping the element on iteration with some other element in the back is also fair. I have learned this in class but I don’t want to be asked how to prove it.
# Difficulty: Easy
# Code

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        num = self.nums.copy()
        res = []
        while num:
            c = random.choice(num)
            num.remove(c)
            res.append(c)
        return res


