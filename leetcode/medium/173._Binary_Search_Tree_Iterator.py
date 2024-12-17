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
        while self.current_location.left is not None:
            self.current_depth.append(self.current_location)
            self.current_location = self.current_location.left

    def __init__(self, root: Optional[TreeNode]):
        self.current_depth = []
        self.current_location = root
        self._toLeftMostSubtree()

    def next(self) -> int:
        res = self.current_location.val
        if self.current_location.right is not None:
            self.current_location = self.current_location.right
            self._toLeftMostSubtree()
        else:
            if self.current_depth:
                self.current_location = self.current_depth.pop()
            else:
                self.current_location = None
        return res

    def hasNext(self) -> bool:
        return self.current_location is not None

