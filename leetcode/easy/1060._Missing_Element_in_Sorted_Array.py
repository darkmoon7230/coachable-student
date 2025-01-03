'''
Link to problem: https://leetcode.com/problems/missing-element-in-sorted-array/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - Just writing it out
Difficulty: Easy

Example case missing 3, 6:
Array: [0,1,2,4,5,7,8]
range: [0,1,2,3,4,5,6]
Diff:  [0,0,0,1,1,2,2]
Points:      ^   ^

The similarity to prefix sum and the later use of binary search should be obvious.

We can see the insertion points are at the "rising edge" of the diff.

When we are missing by 1:
Array: [2,4]
range: [2,3]
Diff:  [0,1]
Point:   ^k={1}

K=1: 2+1=3

When we are missing by more than 1:
Array: [3,6]
Diff:  [0,2]
Points:  ^k={1,2}

K=1: 3+1=4
K=2: 3+2=5

In the middle of the array:
Array: [0,4,5,6,9,...]
range: [0,1,2,3,4,...]
Diff:  [0,3,3,3,5,...]
Point:         ^k={4,5}

K=4: 6+1=7
K=5: 6+2=8

When we are querying outside of the array:
Array: [0,5]
Diff:  [0,4]
Points:     ^k={>4}

K=5: 5+1=6

We can see we are searching for i index in the diff array for k,
we then return array[i - 1] + k - diff[i - 1].

'''

def sortedSearch(arr: List[int], target: int) -> int:
    lo, high = 0, len(arr)
    while lo < high:
        mid = (lo + high) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            high = mid
    return lo

class Linear:
    def missingElement(self, nums: List[int], k: int) -> int:
        # normalize the array
        normalized = [0] * len(nums)

        shift = nums[0]
        for idx in range(len(nums)):
            normalized[idx] = nums[idx] - shift - idx

        idx = sortedSearch(normalized, k)

        if idx >= len(nums):
            return nums[-1] + k - normalized[-1]

        return nums[idx - 1] + k - normalized[idx - 1]

'''
Optimization:
Instead of normalize as another array,
we compute the normalized value when binary search
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def diffAt(idx: int) -> int:
            return nums[idx] - nums[0] - idx

        lo, high = 0, len(nums)
        while lo < high:
            mid = (lo + high) // 2
            if diffAt(mid) < k:
                lo = mid + 1
            else:
                high = mid

        idx = lo
        if idx >= len(nums):
            last_idx = len(nums) - 1
            return nums[last_idx] + k - diffAt(last_idx)
        return nums[idx - 1] + k - diffAt(idx - 1)
