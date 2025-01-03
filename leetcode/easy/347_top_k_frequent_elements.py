# Link to problem: https://leetcode.com/problems/top-k-frequent-elements/
# Loom explaining solution you wrote (5m): https://leetcode.com/problems/top-k-frequent-elements/
# Solution:
# Description:
# Create a frequency map and then solve it as a top k question
# Key ideas
# Frequency map
# Top K
# Diffculty: Easy


from collections import Counter
from heapq import nsmallest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return nsmallest(k, c.keys(), key=lambda k: -c[k])

