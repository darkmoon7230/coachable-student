'''
Link to problem: https://leetcode.com/problems/cutting-ribbons/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - come up with a brute-force idea first when stuck
 - optimize brute-force (replace linear scan with binary search)
 - realize guessing is easier than solving it directly (not stuck on one approach)
Difficulty: Hard
Code
'''

'''
TODO for darek: so is there a dynamic programming/ no guessing way to solve this question?
'''

'''
Bruteforce O(max(ribbons) * k):

Simple for loop, asking:
How many pieces can we get if we aim for this size => is this enough?
'''
class Bruteforce:

    def maxLength(self, ribbons: List[int], k: int) -> int:
        def num_pieces_for(size: int) -> bool:
            num_pieces = 0
            for ribbon in ribbons:
                num_pieces += ribbon // size
            return num_pieces

        # This is an obvious hint for binary search (see below)
        for size in range(max(ribbons), 0, -1):
            if num_pieces_for(size) >= k:
                return size

        return 0

'''
Binary search (optimization over bruteforce):
O(k log(max(ribbons)))

Aim to optimize by asking this question:
"How many pieces can we get if we aim for this size"
As little as possible.

Need to reason through the binary search to avoid infinite loop.
'''
class Solution:

    def maxLength(self, ribbons: List[int], k: int) -> int:
        def num_pieces_for(size: int) -> bool:
            num_pieces = 0
            for ribbon in ribbons:
                num_pieces += ribbon // size
            return num_pieces

        lo, high = 0, max(ribbons) + 1
        while lo < high:
            mid = (high + lo + 1) // 2
            if mid == 0:
                break

            pieces = num_pieces_for(mid)

            if pieces >= k:
                lo = mid
            else:
                high = mid - 1

        return lo
