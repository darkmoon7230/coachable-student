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


def token_of(s):
    cur = ""
    for c in s:
        if c == " ":
            if cur:
                yield int(cur)
                cur = ""
        elif c in "+-*/":
            if cur:
                yield int(cur)
            cur = ""
            yield c
        else:
            assert c.isnumeric()
            cur += c
    if cur:
        yield int(cur)

class Solution:
    def calculate(self, s: str) -> int:
        itr = token_of(s)
        vals = [next(itr)]
        try:
            while True:
                token = next(itr)
                rhs = next(itr)
                match token:
                    case "+":
                        vals.append(rhs)
                    case "-":
                        vals.append(-rhs)
                    case "*":
                        vals.append(vals.pop() * rhs)
                    case "/":
                        vals.append(int(vals.pop() / rhs))
        except StopIteration:
            pass
        return sum(vals)

