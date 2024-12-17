# Link to problem: https://leetcode.com/problems/diagonal-traverse/description/
# Loom explaining solution you wrote (5m): TODO
# Solution:
# Description
# Key ideas
# Reason through the boundary conditions by drawing a bigger square with arrows crossing through them
# There’s nothing difficult but one needs to be extra careful
# Difficulty: Medium
# Code

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def next_up_cord(cord):
            x, y = cord
            return [x + 1, y - 1]

        def next_down_cord(cord):
            x, y = cord
            return [x - 1, y + 1]

        def out_of_bound(cord):
            x, y = cord
            if x < 0 or y < 0:
                return True
            if y >= len(mat):
                return True
            if x >= len(mat[0]):
                return True
            return False

        def at(cord):
            x, y = tuple(cord)
            return mat[y][x]

        up = True
        res = []
        cord = [0, 0]
        while cord != (len(mat[0]), len(mat)):
            while not out_of_bound(cord):
                res.append(at(cord))
                cord = next_up_cord(cord) if up else next_down_cord(cord)

            # Okay now we need to fix the next cord
            if up:
                # Usually it is on top of the next element
                cord[1] += 1
                # However, when its on the edge, we will need to move it in
                if out_of_bound(cord):
                    cord[1] += 1
                    cord[0] -= 1
            else:
                # When coming out of the left edge,
                # the element is should be on the right
                cord[0] += 1
                # When coming out of the bottom,
                # we need to move it in
                if out_of_bound(cord):
                    cord[1] -= 1
                    cord[0] += 1
            up = not up

            if out_of_bound(cord):
                break

        return res


