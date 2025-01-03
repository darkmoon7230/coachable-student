# Link to problem: https://leetcode.com/problems/subsets/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Think recursively
# Difficulty: Extremely Easy
# Code

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        for lst in self.subsets(nums[:-1]):
            res.append(lst)
            res.append(lst + [nums[-1]])
        return res

