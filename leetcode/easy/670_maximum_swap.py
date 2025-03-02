# Link to problem: https://leetcode.com/problems/maximum-swap/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description: 
# Break the number down to digits.
# Search from left to right to swap to the largest number on the right, with a priority on lower digits.
# Difficulty: Easy

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        for i in range(len(digits) - 1):
            max_idx, max_number = max(enumerate(digits[i:]), key=lambda p: (p[1], p[0]))
            max_idx += i
            if digits[i] >= max_number:
                continue
            digits[max_idx], digits[i] = digits[i], digits[max_idx]
            break

        return int("".join(digits))
