# Link to problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# DST
# Difficulty: Easy
# Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0
        q = [(root, 0)]
        while q:
            n, v = q[-1]
            q.pop()

            new_val = v * 10 + n.val

            # Leaf
            if n.left is None and n.right is None:
                res += new_val

            if n.left is not None:
                q.append((n.left, new_val))
            if n.right is not None:
                q.append((n.right, new_val))

        return res


