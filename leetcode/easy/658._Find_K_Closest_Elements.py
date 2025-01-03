'''
Link to problem: https://leetcode.com/problems/find-k-closest-elements/
Loom explaining solution you wrote (5m): see below comments for write out
Solution:
Description
Key ideas
- This is a classic two pointer question
- need to be mindful with the initial binary search landing a value other than x
Difficulty: Easy
'''

def sortedLeftIndexOf(arr: List[int], target: int) -> int:
    lo, high = 0, len(arr)
    while lo < high:
        mid = (high - lo) // 2 + lo
        if arr[mid] < target:
            lo = mid + 1
        else:
            high = mid
    return lo

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def preferLeftIndex(left_idx: int, right_idx: int) -> bool:
            return abs(arr[left_idx] - x) <= abs(arr[right_idx] - x)

        # root index points at the index x will be insert on,
        # which is not necessarily the cloest poistion
        root_idx = sortedLeftIndexOf(arr, x)

        # trivial case:
        # 1. root_idx is on the boundary
        # 2. if arr[root_idx] == x:
        #    we know know values before root_idx is x,
        #    so its safe to use that as starting left idx
        if root_idx == len(arr):
            left_idx, right_idx = root_idx - 1, root_idx
        elif arr[root_idx] == x or root_idx == 0:
            left_idx, right_idx = root_idx, root_idx + 1
        # non-trivial:
        # when arr[root_idx] is not x,
        # we need to see if we should start with root_idx - 1 or root_idx
        #
        # Can be merged to above if/ elif statements, being explicit here
        elif preferLeftIndex(root_idx - 1, root_idx):
            left_idx, right_idx = root_idx - 1, root_idx
        else:
            left_idx, right_idx = root_idx, root_idx + 1

        while right_idx - left_idx < k:
            # trivial case: index on the boundary
            # not applying early stopping to make this more clear
            if right_idx == len(arr):
                left_idx -= 1
            elif left_idx == 0:
                right_idx += 1
            # non-trivial case:
            elif preferLeftIndex(left_idx - 1, right_idx):
                left_idx -= 1
            else:
                right_idx += 1

        return arr[left_idx:right_idx]
