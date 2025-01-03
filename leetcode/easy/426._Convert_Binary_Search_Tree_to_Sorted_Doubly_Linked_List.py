# Link to problem: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Need to realize the ordering of the doubly linked list is the inorder traversal of the binary search tree.
# Note:
# During the interview, it might be best to shove the element order into an array and update the forward/ backward pointer in a separate chunk. Updating references here is error-prone.
# Difficulty: Easy
# Code

class Solution:

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        head = Node(0, None, None)
        # Easier to pass by ref
        cur = [head]

        def _new_node(root: 'Node'):
            cur[0].right = root
            root.left = cur[0]
            cur[0] = root

        def _inorder(root: 'Optional[Node]'):
            if root is None:
                return
            _inorder(root.left)
            right = root.right
            _new_node(root)
            _inorder(right)

        _inorder(root)

        head.right.left = cur[0]
        cur[0].right = head.right

        return head.right

