'''
Leetcode link: https://leetcode.com/problems/range-sum-query-2d-immutable/

Key idea:
- prefix sum
- drawing it down in a sheet

Diffculty: Medium, was hard when I am not familiar with prefix sum

The easiest example is this matrix:
   1 2
\\----
a: 1 2
b: 3 4

If we want to calculate the sum from b2 to b2 (just 4),
we need b2 = a1 + a2 + b1.
Should be obvious that we should be doing something like:
b2 = cumulative[b1] + cumulative[a2] + b2
But cumulative[b1] = a1 + b1, cumulative[a2] = a1 + a2,
therefore b2 would have two duplicative a1, so we need to do:
b2 = cumulative[b1] + cumulative[a2] + b2 - cumulative[a1].

This is how we get a good prefix sum matrix where:
cumulative[y][x] is the sum of all members from [0,0] to [y,x].

When we are working on coming up with the sum,
we need to carve out the portion on the left,
and the portion on the top.
Note that this will mean we got rid of the upper left part twice,
so we will need to add it back in.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cumulative_mtx = [[0] * len(matrix[0]) for _ in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                up = cumulative_mtx[i - 1][j] if i > 0 else 0
                left = cumulative_mtx[i][j - 1] if j > 0 else 0
                dup = cumulative_mtx[i - 1][j - 1] if i > 0 and j > 0 else 0
                cumulative_mtx[i][j] = up + left + matrix[i][j] - dup

        self.cumulative_mtx = cumulative_mtx

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        lower_right_v = self.cumulative_mtx[row2][col2]
        upper_left_anchor_v = self.cumulative_mtx[row1 - 1][col1 - 1] if row1 * col1 != 0 else 0
        left_cols_v = self.cumulative_mtx[row2][col1 - 1] if col1 > 0 else 0
        upper_rows_v = self.cumulative_mtx[row1 - 1][col2] if row1 > 0 else 0
        return lower_right_v - left_cols_v - upper_rows_v + upper_left_anchor_v


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)