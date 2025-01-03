# Link to problem: https://leetcode.com/problems/powx-n/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# For n < 1, pow(x, n) = 1/pow(x,-n)
# If both x and n are int, we can finish this computation in O(1) using bitshift and add/subtract only.
# We can cache the exponential number to reduce the number of computation, should be reduced to o(log N). 
# If x is int, we can take away the cache and replace it with bitshift.
# Difficulty: Easy
# Code


from math import log2, floor

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 0:
            return 1.0

        cache = [x]
        for i in range(floor(log2(n))):
            cache.append(cache[i] * cache[i])

        res = 1.0
        while n > 0:
            i = floor(log2(n))
            res *= cache[i]
            n = n - 2**i

        return res


