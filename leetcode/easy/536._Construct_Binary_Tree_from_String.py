# Link to problem: https://leetcode.com/problems/construct-binary-tree-from-string
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Recursive parsing
# A stack based iterative approach also works
# Difficulty: Easy
# Code

from itertools import takewhile

class Solution:
    def parseNumber(self):
        digits = list(takewhile(lambda c: c.isdigit() or c == "-", self.s[self.cur:]))
        self.cur += len(digits)
        return int("".join(digits))

    def parseNode(self):
        node = TreeNode(self.parseNumber())
        if self.cur < len(self.s) and self.s[self.cur] == "(":
            self.cur += 1  # (
            node.left = self.parseNode()
            self.cur += 1  # )
        if self.cur < len(self.s) and self.s[self.cur] == "(":
            self.cur += 1  # (
            node.right = self.parseNode()
            self.cur += 1  # )
        return node

    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return None
        self.s = s
        self.cur = 0
        return self.parseNode()


