# Link to problem: https://leetcode.com/problems/find-largest-value-in-each-tree-row
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Level order traversal
# Diffculty: Easy
# Code

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        cur_level = 0
        cur_level_largest = -float('inf')

        q = deque([(root, 0)])
        while q:
            cur, depth = q[0]
            q.popleft()

            if cur is None:
                continue

            cur_v = cur.val
            if depth > cur_level:
                res.append(cur_level_largest)
                cur_level = depth
                cur_level_largest = cur.val
            elif cur_v > cur_level_largest:
                cur_level_largest = cur_v

            next_level = depth + 1
            q.append((cur.left, next_level))
            q.append((cur.right, next_level))

        return res + [cur_level_largest]

