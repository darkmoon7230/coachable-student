# Link to problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# See “Lowest Common Ancestor of a Binary Tree III” above
# We can also reduce this question to “Lowest Common Ancestor of a Binary Tree III” by constructing a hash map that map a node to its parent. Would be more performant to presenting implementation
# Difficulty: Easy
# Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def _path_to(root: 'TreeNode', n: 'TreeNode'):
    q = [(root, [])]
    while q:
        c, path = q[0]
        q.pop(0)

        new_path = path + [c]
        if c == n:
            return new_path

        if c.left is not None:
            q.append((c.left, new_path))
        if c.right is not None:
            q.append((c.right, new_path))

    pass

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = _path_to(root, p)
        q_path = _path_to(root, q)

        last_common = 0
        for p_n, q_n in zip(p_path, q_path):
            if p_n == q_n:
                last_common += 1
            else:
                break

        return p_path[last_common - 1]

