# Link to problem: https://leetcode.com/problems/exclusive-time-of-functions/description/
# Loom explaining solution you wrote (5m): TODO
# Solution:
# Description
# Key ideas
# Start and end have different inclusive behavior (end has diff + 1)
# Keeping track of a prev time helps a lot
# Difficulty: Medium 
# Code

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        prev_segments = []
        messages = [tuple(msg.split(":")) for msg in logs]
        messages = [(int(func), state, int(end)) for func, state, end in messages]
        prev_time = 0
        for func, state, end in messages:
            duration = end - prev_time
            if state == "start":
                if prev_segments:
                    res[prev_segments[-1][0]] += duration
                prev_segments.append((func, state, end))
                prev_time = end
            else:
                res[prev_segments[-1][0]] += duration + 1
                prev_time = end + 1
                prev_segments.pop()
        return res



