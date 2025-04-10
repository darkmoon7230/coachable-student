"""
Loom: https://www.loom.com/share/a3c5f5f29efa4a6ea22c9c26c949de63?sid=cad61fe0-89f1-4b0d-945f-3332a21df317

   /-> 2 \
0 -> 1 -> 4
   \-> 3 /

0 -> 1
2 -> 3

N = # nodes in the graph

path = []
q = []
while q:  # N^2
    node = q.pop() # copy path may take N
    path.append(node)
    if node is target:
        result.append(list(path)) # O(N)

    visit neighbor of node by pushing them into q
    path.pop()

back tracking.

rec(node, path): # N
    if node is target
        ...
    path.append(node)
    for neighbor of node:
        rec(nieghbor, path)
    path.pop()

"""

"""
[[1],[],[3],[]]
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []  #
        path = []  #

        def visit(node):  #
            if node == (len(graph) - 1):
                result.append(list(path) + [node])
                return
            path.append(node)
            for neighbor in graph[node]:
                visit(neighbor)
            path.pop()

        visit(0)
        return result


