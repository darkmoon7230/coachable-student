# Link to problem: https://leetcode.com/problems/basic-calculator-ii/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# To step process, process */ first, +- last.
# - can be treated as + (-val), +- can be mapped as sum
# When processing */, use a value stack
# Difficulty: Medium
# Code

# extracting this out helps with emphasesing/ delgating:
# 1. typo
# 2. meaning of "+-*/"
ADD_OP = "+"
MINUS_OP = "-"
MULTIPLY_OP = "*"
DIVISION_OP = "/"
VALID_OP = set([ADD_OP, MINUS_OP, MULTIPLY_OP, DIVISION_OP])

def tokenize(s) -> List[str]:
    res = []
    cur = ""
    for c in s.replace(" ", ""):
        if c in VALID_OP:
            if cur:
                res.append(int(cur))
            cur = ""
            res.append(c)
        else:
            assert c.isnumeric()
            cur += c
    if cur:
        res.append(int(cur))
    return res

class Solution:
    def calculate(self, s: str) -> int:
        tokens = tokenize(s)
        vals = [tokens.pop(0)]
        # leetcode does not support this yet
        # for token, rhs in batched(tokens, 2):
        while tokens:
            operator = tokens.pop(0)
            rhs = tokens.pop(0)
            match operator:
                case ADD_OP:
                    vals.append(rhs)
                case MINUS_OP:
                    vals.append(-rhs)
                case MULTIPLY_OP:
                    vals.append(vals.pop() * rhs)
                case DIVISION_OP:
                    vals.append(int(vals.pop() / rhs))
        return sum(vals)

