# Link to problem: https://leetcode.com/problems/binary-search-tree-iterator/
# Loom explaining solution you wrote (5m): TODO
# Solution:
# Description
# Key ideas
# This is the same as iterative in-order processing
# The best way to solve this question is to draw serval BSTs and reason through them.
# Difficulty: Medium
# Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def _toLeftMostSubtree(self):
        while self.current.left is not None:
            self.current_depth.append(self.current)
            self.current = self.current.left

    def __init__(self, root: Optional[TreeNode]):
        self.current_depth = []
        self.current = root
        self._toLeftMostSubtree()

    def next(self) -> int:
        res = self.current.val
        if self.current.right is not None:
            self.current = self.current.right
            self._toLeftMostSubtree()
        else:
            if self.current_depth:
                self.current = self.current_depth.pop()
            else:
                self.current = None
        return res

    def hasNext(self) -> bool:
        return self.current is not None

