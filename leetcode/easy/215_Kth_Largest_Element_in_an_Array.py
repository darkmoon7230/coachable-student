import heapq

# Description
# Maintain min heap of size k and keep pushing and popping if full
# Key ideas: Min heap 
# Note that we can simply use nlargest
# Difficulty: Extremely Easy

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)

        for ele in nums[k:]:
            heapq.heappushpop(pq, ele)

        return pq[0]

