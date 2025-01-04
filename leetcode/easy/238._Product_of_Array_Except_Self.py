'''
https://leetcode.com/problems/product-of-array-except-self/

keypoint:
 - prefix sum
 - start with an 3-element array example

Diffculty: Easy
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rhs_arr = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            rhs_arr[i] = rhs_arr[i + 1] * nums[i + 1]

        lhs_arr = [1]
        for i in range(0, len(nums) - 1):
            lhs_arr.append(lhs_arr[-1] * nums[i])

        return [rhs * lhs for (rhs, lhs) in zip(rhs_arr, lhs_arr)]
