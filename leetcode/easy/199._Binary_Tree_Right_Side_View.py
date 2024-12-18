# Link to problem: https://leetcode.com/problems/binary-tree-right-side-view/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Level order traversal
# The right-most node of each level is the “right side view”
# Difficulty: Easy
# Code


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _level_order(root: TreeNode):
    current_level = 0
    current_level_nodes = []

    q = [(root, 0)]
    while q:
        n, lev = q[0]
        q.pop(0)

        if current_level == lev:
            current_level_nodes.append(n)
        else:
            yield current_level_nodes
            current_level = lev
            current_level_nodes = [n]

        next_lev = lev + 1
        if n.left is not None:
            q.append((n.left, next_lev))
        if n.right is not None:
            q.append((n.right, next_lev))
    yield current_level_nodes

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        for level in _level_order(root):
            res.append(level[-1].val)
        return res

