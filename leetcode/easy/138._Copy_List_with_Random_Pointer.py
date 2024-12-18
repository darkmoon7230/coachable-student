# Link to problem: https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Two passes
# one map the old node to the new
# Next mirror the structure of the old list
# Difficulty: Extremely Easy
# Code

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        mapping = dict()
        cur = head
        while cur is not None:
            mapping[cur] = Node(cur.val)
            if cur.random and cur.random not in mapping:
                mapping[cur.random] = Node(cur.random.val)
            cur = cur.next

        cur = head
        while True:
            m = mapping[cur]
            if cur.random is not None:
                m.random = mapping[cur.random]
            if cur.next is not None:
                m.next = mapping[cur.next]
            else:
                break
            cur = cur.next

        return mapping[head]

