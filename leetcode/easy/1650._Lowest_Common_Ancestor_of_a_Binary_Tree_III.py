# Link to problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Construct a path from one node to the parent
# Against the other node, find the path to the root, while going up, check if the visiting node is in the path of the other, return first
# Note:
# We can find the depth of the two node and align the depth first to reduce the size of the path set, so less memory usage and faster speed
# Difficulty: Very Easy

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_s = set()
        p_cur = p
        while p_cur:
            p_s.add(p_cur)
            p_cur = p_cur.parent

        q_cur = q
        while q_cur:
            if q_cur in p_s:
                return q_cur
            q_cur = q_cur.parent
        pass
