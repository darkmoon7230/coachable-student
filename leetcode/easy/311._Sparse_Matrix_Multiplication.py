'''
Link to problem: https://leetcode.com/problems/sparse-matrix-multiplication/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - Remeber how matrix multiplication works
 - identify where to optimize
Difficulty: Easy
'''

'''
Bruteforce/ Generic multiply:
'''

class Generic:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(len(mat2))])

        return res

'''
Note we will not be able to optimize big-o.
And optimizing a usually highly optimized loop can be tricky.
So the idea here is obvious:
skipping computation when either respective row/ col in either matrix is 0
'''

from collections import defaultdict

class Solution:
    def multiply(self, mat_a: List[List[int]], mat_b: List[List[int]]) -> List[List[int]]:
        # this could technically be a dict of list of pairs
        # using dict of dict is just more ergonomic

        rows_a = defaultdict(dict)
        for row_i, row in enumerate(mat_a):
            for col_i, val in enumerate(mat_a[row_i]):
                if val != 0:
                    rows_a[row_i][col_i] = val

        cols_b = defaultdict(dict)
        for row_i, col_i in product(range(len(mat_b)), range(len(mat_b[0]))):
            if (val := mat_b[row_i][col_i]) != 0:
                cols_b[col_i][row_i] = val

        res = [[0] * len(mat_b[0]) for _ in range(len(mat_a))]

        for i in range(len(res)):
            for j in range(len(res[0])):
                for col in rows_a[i]:
                    if col in cols_b[j]:
                        res[i][j] += rows_a[i][col] * cols_b[j][col]

        return res
