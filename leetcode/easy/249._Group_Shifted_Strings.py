# Link to problem: https://leetcode.com/problems/group-shifted-strings/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Need to realize we need to group by the relative ordering of letters
# Need to normalize negative/ zero difference
# Difficulty: Easy
# Code

from itertools import groupby

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def mapToCharDiff(s: str) -> List[int]:
            raw_ord = [ord(c) for c in s]
            diff_ord = [e - raw_ord[0] for e in raw_ord]
            normalized = [val if val >= 0 else val + 26 for val in diff_ord]
            # print(s, "->", normalized)
            return tuple(normalized)

        strings.sort(key=mapToCharDiff)
        res = []
        for _, g in groupby(strings, key=mapToCharDiff):
            res.append(list(g))

        return res

