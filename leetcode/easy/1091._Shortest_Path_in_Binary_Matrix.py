# Link to problem: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# BST search
# Difficulty: Easy
# Code

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        edge_n = len(grid) - 1

        if 1 in [grid[0][0], grid[edge_n][edge_n]]:
            return -1

        q = [((0, 0), [])]
        visited = set()
        while q:
            cord, path = q[0]
            q.pop(0)

            if cord == (edge_n, edge_n):
                return len(path) + 1

            if cord in visited:
                continue
            else:
                visited.add(cord)

            new_path = path + [cord]
            for diff_x, diff_y in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_x, new_y = cord[0] + diff_x, cord[1] + diff_y

                if new_x < 0 or new_x > edge_n:
                    continue
                if new_y < 0 or new_y > edge_n:
                    continue

                if grid[new_x][new_y] == 1:
                    continue

                q.append(((new_x, new_y), new_path))


        return -1


