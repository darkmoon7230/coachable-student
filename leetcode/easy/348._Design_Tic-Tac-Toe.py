# Link to problem: https://leetcode.com/problems/design-tic-tac-toe/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# This is just coding at this point, there’s no difficulty
# We can avoid using two bards, we can also keep track of the diagonals in a specific array instead of zig-zagging
# Difficulty: Easy
# Code

def _check_win_cond(b, point):
    x, y = point
    # Axises
    if all(b[y]):
        return True

    if all([b[i][x] for i in range(len(b))]):
        return True

    # left-right cross
    if x == y and all([b[i][i] for i in range(len(b))]):
        return True

    # right-left cross
    sz = len(b) - 1
    if (x == sz - y) and all([b[i][sz - i] for i in range(len(b))]):
        return True

    return False

class TicTacToe:

    def __init__(self, n: int):
        self.p1 = [[False] * n for _ in range(n)]
        self.p2 = [[False] * n for _ in range(n)]


    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1[row][col] = True
            if _check_win_cond(self.p1, (col, row)):
                return 1
        else:
            self.p2[row][col] = True
            if _check_win_cond(self.p2, (col, row)):
                return 2
        return 0


