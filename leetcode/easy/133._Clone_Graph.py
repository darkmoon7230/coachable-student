# Link to problem: https://leetcode.com/problems/clone-graph/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Basically: 138. Copy List with Random Pointer
# Code

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        def dst(f):
            visited = set()
            q = [node]
            while q:
                cur = q[-1]
                q.pop()

                if cur in visited:
                    continue
                visited.add(cur)

                f(cur)

                for neighbor in cur.neighbors:
                    q.append(neighbor)

        # generate mapping
        def genMapping(n):
            mapping[n] = Node(n.val)

        mapping = dict()
        dst(genMapping)

        # redirect mapping
        def redirectMapping(n):
            mapped = mapping[n]
            for neighbor in n.neighbors:
                mapped.neighbors.append(mapping[neighbor])
        dst(redirectMapping)

        return mapping[node]


