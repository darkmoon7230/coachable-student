'''
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

Key:
 - Prefix sum

Diffculty: Easy
'''

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        running_sum = max_length = 0
        diff_map = {0: -1}

        for i, num in enumerate(nums):
            running_sum += num

            if running_sum not in diff_map:
                diff_map[running_sum] = i

            complement = running_sum - k
            if complement in diff_map:
                max_length = max(max_length, i - diff_map[complement])

        return max_length

