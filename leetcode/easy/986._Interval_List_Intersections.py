# Link to problem: https://leetcode.com/problems/interval-list-intersections/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# It is irrelevant if an interval is in A and B
# (Again) The first step to solve most of intervals is to sort the intervals
# Always check if previous interval is bigger than the current interval
# Difficulty: Harder Easy
# Code

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        merged = sorted(firstList + secondList)
        res = []
        last_end = merged[0][1]
        for interval in merged[1:]:
            # Overlaps
            if last_end >= interval[0]:
                # Emits the overlapping section
                res.append([interval[0], min(last_end, interval[1])])
                last_end = max(last_end, interval[1])
            else:
                last_end = interval[1]
        return res

