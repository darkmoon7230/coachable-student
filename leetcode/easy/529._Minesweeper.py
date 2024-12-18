# Link to problem: https://leetcode.com/problems/minesweeper/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Graph Traversal
# Difficulty: Easy
# Code

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def out_of_bound(pos):
            if not 0 <= pos[0] < len(board):
                return True
            if not 0 <= pos[1] < len(board[0]):
                return True
            return False

        def check_mine(pos):
            res = 0
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    cord = pos[0] + x_diff, pos[1] + y_diff
                    if out_of_bound(cord):
                        continue
                    if at(cord) == "M":
                        res += 1
            return res

        def at(click):
            return board[click[0]][click[1]]

        def update(click, val):
            board[click[0]][click[1]] = val

        if at(click) == "M":
            update(click, "X")
            return board

        # clicked on a E, we need to reveal tiles
        q = [tuple(click)]
        visited = set()
        while q:
            cur = q[-1]
            q.pop()

            if out_of_bound(cur) or (cur in visited):
                continue
            visited.add(cur)

            if (mine_num := check_mine(cur)) > 0:
                update(cur, str(mine_num))
                continue

            update(cur, "B")
            for x_diff in [-1, 0, 1]:
                for y_diff in [-1, 0, 1]:
                    q.append((cur[0] + x_diff, cur[1] + y_diff))

        return board


