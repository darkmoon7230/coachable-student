# Link to problem: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
# Loom explaining solution you wrote (5m):  See comments
# Solution:
# Description
# Key ideas
# Understand the edge case where the number rolls-over
# DIfficulty: Easy
# Code

def _link_node(prev, insertVal):
    n = Node(insertVal)
    original_next = prev.next
    prev.next = n
    n.next = original_next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            res = Node(insertVal)
            res.next = res
            return res

        # Keep track of the edge (high -> low)
        edge = head

        prev = head
        cur = head.next
        # Main loop
        while cur != head:
            if cur.val < prev.val:
                edge = prev

            if prev.val <= insertVal < cur.val:
                _link_node(prev, insertVal)
                return head

            prev = cur
            cur = cur.next

        # Extra loop for the head node
        if cur.val < prev.val:
            edge = prev
        if prev.val <= insertVal < cur.val:
            _link_node(prev, insertVal)
            return head

        # Okay we are on the boundary
        _link_node(edge, insertVal)
        return head

