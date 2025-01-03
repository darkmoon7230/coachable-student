'''
Link to problem: https://leetcode.com/problems/3sum/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - Be plain in terms of approach, with unfamiliar question write out the most 
   intuitive brute-force close solution first.
 - Optimize the problem with Big-O
Difficulty: Medium (was hard), mainly due to optimizing timeout.
'''

def containsInSorted(arr: List[int], target: int) -> bool:
    lo, high = 0, len(arr)
    while lo < high:
        mid = (lo + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid
        else:
            lo = mid + 1
    return 0 <= lo < len(arr) and arr[lo] == target

'''
Double for-loop + binary search, O(N^2 log N)
De-dup through set
'''
class BinarySearch:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = set()
        for first_idx, first_val in enumerate(nums):
            if first_val > 0:
                break
            if first_idx > 0 and nums[first_idx - 1] == first_val:
                continue

            for second_idx, second_val in enumerate(nums[first_idx + 1:], first_idx + 1):
                third_val = (first_val + second_val) * -1

                if containsInSorted(nums[second_idx + 1:], third_val):
                    res.add(tuple(sorted([first_val, second_val, third_val])))

        return [list(t) for t in res]

'''
Double for-loop + dict, O(N^2)
De-dup through set
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        nums_map = dict()
        for idx, num in enumerate(nums):
            # use the last index
            nums_map[num] = idx

        res = set()
        for first_idx, first_val in enumerate(nums):
            if first_val > 0:
                break
            if first_idx > 0 and nums[first_idx - 1] == first_val:
                continue

            for second_idx, second_val in enumerate(nums[first_idx + 1:], first_idx + 1):
                third_val = (first_val + second_val) * -1

                if third_val in nums_map and nums_map[third_val] > second_idx:
                    res.add(tuple(sorted([first_val, second_val, third_val])))

        return [list(t) for t in res]
