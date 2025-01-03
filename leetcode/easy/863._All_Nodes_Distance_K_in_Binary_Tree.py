# Link to problem: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Its trivial to discover distanceK below target
# We need to construct forward path to explore nodes above target
# Parent map via BST/ DST
# Difficulty: Easy
# Code

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = dict()
        q = [root]
        while q:
            cur = q[0]
            q.pop(0)

            if cur == target:
                break

            if cur.left is not None:
                parentMap[cur.left] = cur
                q.append(cur.left)

            if cur.right is not None:
                parentMap[cur.right] = cur
                q.append(cur.right)

        res = []
        q = [(target, k)]
        visited = set()
        while q:
            node, distance = q[-1]
            q.pop()

            if node in visited:
                continue
            else:
                visited.add(node)

            if distance == 0:
                res.append(node.val)
                continue

            if node in parentMap:
                q.append((parentMap[node], distance - 1))
            if node.left is not None:
                q.append((node.left, distance - 1))
            if node.right is not None:
                q.append((node.right, distance - 1))
        return res


