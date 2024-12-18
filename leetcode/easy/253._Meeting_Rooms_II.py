# Link to problem: https://leetcode.com/problems/meeting-rooms-ii/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# Interval scheduling problem usually involves sorting all the intervals with respective to the starting time.
# This is not intuitive but is generally the solution
# Reduce this problem down removing non-competing rooms through iterations, answer is the number of iteration
# Difficulty: Easy
# Code

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        while intervals:
            rejected = []
            currently_occupied_till = None
            for start, end in intervals:
                if currently_occupied_till is None or currently_occupied_till <= start:
                    currently_occupied_till = end
                else:
                    rejected.append((start, end))
            res += 1
            intervals = rejected
        return res
