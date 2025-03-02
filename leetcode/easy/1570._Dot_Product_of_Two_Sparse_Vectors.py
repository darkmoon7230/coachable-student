# Link to problem: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# For all elements, if any of the two vectors the number is 0, no computation is needed.
# Sparse vector is a vector where the elements are predominantly 0
# We are running against a very easy for loop,
# To top that we need to do as little overhead as possible.
# Difficulty: Easy
# Code


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mask = [n != 0 for n in nums]

        # print(self.nums_compress)
        # self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        compute_mask = [lhs and rhs for (lhs, rhs) in zip(self.mask, vec.mask)]
        res = 0
        for idx, mask in enumerate(compute_mask):
            if mask:
                res += self.nums[idx] * vec.nums[idx]
        return res

        # res = 0
        # for a, b in zip(self.nums, vec.nums):
        #     res += a * b
        # return res
