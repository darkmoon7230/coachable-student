# Link to problem: https://leetcode.com/problems/diagonal-traverse/description/
# Loom explaining solution you wrote (5m): TODO
# Solution:
# Description
# Key ideas
# Reason through the boundary conditions by drawing a bigger square with arrows crossing through them
# There’s nothing difficult but one needs to be extra careful
# Difficulty: Medium
# Code

from enum import Enum

# We build a state machine to describe the walk process
class State(Enum):
    UP_RIGHT = 0
    UP_RIGHT_FIX = 1
    DOWN_LEFT = 2
    DOWN_LEFT_FIX = 3

# Yes these vectores does tell us that up-right and down-left
# operations are just rotated versions of each other
UP_RIGHT_DIRECTION = (-1, 1)
UP_RIGHT_FIX_CEIL = (1, 0)
UP_RIGHT_FIX_SIDE = (2, -1)

DOWN_LEFT_DIRECTION = (1, -1)
DOWN_LEFT_FIX_SIDE = (0, 1)
DOWN_LEFT_FIX_BOTTOM = (-1, 2)


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def piecewise_add(base: tuple[int], diff: tuple[int]) -> tuple[int]:
            return base[0] + diff[0], base[1] + diff[1]

        def out_of_bound(cord: tuple[int]) -> bool:
            y, x = cord
            return not (0 <= y < len(mat)) or not (0 <= x < len(mat[0]))

        def at(cord: tuple[int]) -> int:
            print(cord)
            y, x = cord
            return mat[y][x]

        state = State.UP_RIGHT
        cord = (0, 0)
        target = (len(mat) - 1, len(mat[0]) - 1)
        res = []
        while cord != target:
            match (state):
                case State.UP_RIGHT:
                    res.append(at(cord))
                    cord = piecewise_add(cord, UP_RIGHT_DIRECTION)
                    if out_of_bound(cord):
                        state = State.UP_RIGHT_FIX
                case State.UP_RIGHT_FIX:
                    # overflow from the side
                    if cord[1] == len(mat[0]):
                        cord = piecewise_add(cord, UP_RIGHT_FIX_SIDE)
                    else:
                        cord = piecewise_add(cord, UP_RIGHT_FIX_CEIL)
                    state = State.DOWN_LEFT
                case State.DOWN_LEFT:
                    res.append(at(cord))
                    cord = piecewise_add(cord, DOWN_LEFT_DIRECTION)
                    if out_of_bound(cord):
                        state = State.DOWN_LEFT_FIX
                case State.DOWN_LEFT_FIX:
                    if cord[0] == len(mat):
                        cord = piecewise_add(cord, DOWN_LEFT_FIX_BOTTOM)
                    else:
                        cord = piecewise_add(cord, DOWN_LEFT_FIX_SIDE)
                    state = State.UP_RIGHT
        res.append(at(cord))
        return res


