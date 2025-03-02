# Link to problem: https://leetcode.com/problems/merge-intervals/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# For most of the interval questions, sorting the interval trivializes the question.
# Difficulty: Easy
# Code

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            prev = res[-1]
            if prev[-1] >= interval[0]:
                # overlapping
                res.pop()
                interval[0] = prev[0]
                interval[1] = max(prev[1], interval[1])
            res.append(interval)
        return res
