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
        while self._current.left is not None:
            self._current_depth.append(self._current)
            self._current = self._current.left

    def __init__(self, root: Optional[TreeNode]):
        self._current_depth = []
        self._current = root
        self._toLeftMostSubtree()

    def next(self) -> int:
        res = self._current.val
        if self._current.right is not None:
            self._current = self._current.right
            self._toLeftMostSubtree()
        else:
            if self._current_depth:
                self._current = self._current_depth.pop()
            else:
                self._current = None
        return res

    def hasNext(self) -> bool:
        return self._current is not None

