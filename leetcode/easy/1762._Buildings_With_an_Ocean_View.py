# Link to problem: https://leetcode.com/problems/buildings-with-an-ocean-view/description/
# Loom explaining solution you wrote (5m): https://www.loom.com/share/2a608fffab994b5ea67ef95410215e66
# Solution:
# Description
# Key ideas
# This is basically a: “is this element larger than every number to its right”
# Difficulty: Extremely Easy

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        res = []
        for idx, val in list(enumerate(heights))[::-1]:
            if val > max_height:
                max_height = val
                res.append(idx)
        return res[::-1]
