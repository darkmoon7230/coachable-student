# Link to problem: https://leetcode.com/problems/add-bold-tag-in-string/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Generate a mask for all matching string
# Reduce this problem to a edge detection problem
# Difficulty: Easy
# Code

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        mask = [False] * len(s)
        for word in words:
            idx = -1
            while (idx := s.find(word, idx + 1)) != -1:
                mask[idx:idx + len(word)] = [True] * len(word)

        res = []
        prev = False
        prev_idx = 0
        for idx, val in enumerate(mask):
            if val == prev:
                continue

            res += s[prev_idx:idx]
            if not prev:  # Entering bold area
                res.append("<b>")
            else:  # Exit bold area
                res.append("</b>")

            prev = val
            prev_idx = idx

        res.append(s[prev_idx:])
        if prev:
            res.append("</b>")

        return "".join(res)

