# Link to problem: https://leetcode.com/problems/max-area-of-island/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Basically 200. Number of Islands, but counts the size as well
# Difficulty: Easy
# Code

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def count_island(cord):
            size = 0
            q = [cord]
            while q:
                x, y = q[-1]
                q.pop()

                if not 0 <= x < len(grid[0]):
                    continue
                if not 0 <= y < len(grid):
                    continue

                if grid[y][x] == 0:
                    continue
                grid[y][x] = 0

                size += 1

                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
            return size

        max_size = 0

        for y, y_lst in enumerate(grid):
            for x, ele in enumerate(grid[y]):
                if ele == 1:
                    max_size = max(max_size, count_island((x, y)))
        return max_size
