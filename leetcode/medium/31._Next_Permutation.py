'''
Leetcode: https://leetcode.com/problems/next-permutation/

The key is simply to reason through the question.

Diffculty: Medium, idk why I spent so much time on this.

Basical idea:
partition this question:
e.g. for 1231
We see if 31 is at its max permutation
It is because its descending across all digits.

We see if 231 is at its max permutation, no it is not.
okay we now swap 2 with the immediately bigger value in [3,1] 3.
then sort the right hand side.

The best big-o complexity is O(N), due to the initial check.
All subsequent besides flipping the array
(lookup immediately bigger number, insertion),
could be done using binary search.
'''

'''
Find the start of the descendingly sorted section from right
'''
def rfind_sorted_start(nums: List[int]) -> int:
    prev_max = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < prev_max:
            return i + 1
        prev_max = nums[i]
    return 0

def find_immediately_bigger_index(nums: List[int], target: int, lo: int) -> int:
    for idx in range(lo, len(nums)):
        if nums[idx] <= target:
            return idx - 1
    return len(nums) - 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_section = rfind_sorted_start(nums)
        if max_section == 0:
            # max state of this string
            nums[:] = reversed(nums)
            return

        prev_val = nums[max_section - 1]
        imm_big_idx = find_immediately_bigger_index(nums, prev_val, max_section)
        imm_big_val = nums[imm_big_idx]

        # okay we now need to swap prev_val with imm_big_val,
        # and then sort the nums[max_section:] asscending
        nums[max_section - 1], nums[imm_big_idx] = imm_big_val, prev_val

        # yes this could be a reverse + binary insertion.
        nums[max_section:] = sorted(nums[max_section:])
