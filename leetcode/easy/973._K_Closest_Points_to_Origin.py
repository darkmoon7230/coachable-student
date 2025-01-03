# Link to problem: https://leetcode.com/problems/k-closest-points-to-origin/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Sort with custom comparator
# Note: why is this medium, is there some nuance I am not seeing?
# Difficulty: Extremely Easy
# Code

from heapq import nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(lst):
            x = lst[0]
            y = lst[1]
            return (x**2 + y**2)

        return nsmallest(k, points, key=dist)


