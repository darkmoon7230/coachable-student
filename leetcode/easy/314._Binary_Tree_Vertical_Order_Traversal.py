# Link to problem:  https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
# Loom explaining solution you wrote (5m): https://www.loom.com/share/d7484624a858478185a525f2a562a72b
# Solution:
# Description
# Key ideas
# Iterate through the tree
# On every lowering, mark the position of the child node by computing the position against parent node
# Left is -1, Right is 1
# Use a map to group the nodes of same position
# Difficulty: Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res_d = defaultdict(list)
        q = [(0, root)]
        while q:
            cur_pos, cur_n = q[0]
            q.pop(0)

            res_d[cur_pos].append(cur_n.val)

            if cur_n.left is not None:
                q.append((cur_pos - 1, cur_n.left))

            if cur_n.right is not None:
                q.append((cur_pos + 1, cur_n.right))

        return [val for _, val in sorted(res_d.items())]

