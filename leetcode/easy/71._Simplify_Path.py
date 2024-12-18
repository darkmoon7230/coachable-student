# Link to problem: https://leetcode.com/problems/simplify-path/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Simply use a stack to keep track of what folder we are currently at
# On directory entry, push new path element into the stack
# On directory exit, pop the stack
# Difficulty: Extremely Simple
# Code

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part in ["", "."]:
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)

