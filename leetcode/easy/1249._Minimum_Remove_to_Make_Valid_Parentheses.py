# Link to problem: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Loom explaining solution you wrote (5m): https://www.loom.com/share/31ad82e646ba4e3b96b133bcfdb3527f
# Solution:
# Description
# Key ideas
# Generate a list of parenthese index to remove (using a stack)
# Then generate a new string without those parentheses
# Difficulty: Very Easy

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q = []
        for idx, c in enumerate(s):
            if c not in "()":
                continue
            if not q or c == "(":
                q.append((c, idx))
            else:
                assert c == ")"
                lst_c, _ = q[-1]
                if lst_c == "(":
                    q.pop()
                else:
                    q.append((c, idx))
            pass

        res = ""
        last_idx = -1
        for _, idx in q:
            res += s[last_idx + 1:idx]
            last_idx = idx
        res += s[last_idx + 1:]

        return res
