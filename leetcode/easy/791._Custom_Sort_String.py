# Link to problem: https://leetcode.com/problems/custom-sort-string/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# There’s a key parameter on the sort function
# Note order of undefined character against the order parameter is undefined.
# Difficulty: Extremely Easy
# Code

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_d = dict()
        for idx, val in enumerate(order):
            order_d[val] = idx
        s = list(s)
        s.sort(key=lambda x: order_d[x] if x in order_d else 0)
        return "".join(s)

