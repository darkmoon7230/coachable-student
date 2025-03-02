# Link to problem: https://leetcode.com/problems/nested-list-weight-sum/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# This is a simple nested computation.
# Difficulty: Extremely Easy
# Code

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def cal(ele, depth):
            if ele.isInteger():
                return ele.getInteger() * depth
            else:
                return sum([cal(n, depth + 1) for n in ele.getList()])
        return sum([cal(n, 1) for n in nestedList])

