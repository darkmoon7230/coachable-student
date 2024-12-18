# Link to problem: https://leetcode.com/problems/number-of-islands/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# This is another classic count distinct graphs problem.
# Both BST and DST will work here
# Mark visited tile by directly assign it to a 0
# Diffculty: Easy
# Code

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(start):
            q = [start]
            while q:
                x, y = q[-1]
                q.pop()

                if not 0 <= x < len(grid[0]):
                    continue
                if not 0 <= y < len(grid):
                    continue

                if grid[y][x] == "0":
                    continue
                grid[y][x] = "0"

                # Up
                q.append((x, y + 1))
                # Down
                q.append((x, y - 1))
                # Right
                q.append((x + 1, y))
                # Left
                q.append((x - 1, y))

        count = 0
        for j, line in enumerate(grid):
            for i, c in enumerate(line):
                if c == "1":
                    mark((i, j))
                    count += 1
        return count

