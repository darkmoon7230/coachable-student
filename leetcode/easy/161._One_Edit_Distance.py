# Link to problem: https://leetcode.com/problems/one-edit-distance/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# There two kinds of error: 
# Aligned but mismatch
# Misaligned
# Difficulty: Easy
# Code

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_diff = abs(len(s) - len(t))

        if len_diff > 1:
            return False

        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len_diff == 0:
                    return s[i + 1:] == t[i + 1:]
                if len_diff == 1:
                    if len(s) > len(t):
                        print(s[i + 1:], t[i])
                        return s[i + 1:] == t[i:]
                    else:
                        print(t[i + 1:], s[i])
                        return t[i + 1:] == s[i:]

        return len_diff != 0

