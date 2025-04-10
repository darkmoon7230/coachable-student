"""
Parital recording:
https://www.loom.com/share/e05c1431cbed455fb7ee4cdfe6ae11af

Pick three numbers such that sum(nums) = 0

Base examples:
[-1,0,1,2,-1,-4]

Combinations: 2
[-1, -1, 0]
[-1, -1, 2]

Everything is +/-
[1,1,1] => []
[-1,-1,-1] => []
[1,2,3]

If everything is the same sign, there will be no result.

We will need to find sign complenets.
+,-,- => ordering => sorting

[-2,-1,-6,3,4,2]
[-6, 4, 2], [3, -2, -1]

[0,2,4,5,-5,-2,-1]
[0, 2, -2]

[-1,-1,-1,0,1,1,1] => [-1, 0, 1]

[-6, 4 ,2, 0] => [-6, 4, 2]

Edge:
[0, 1, 1] => []
[0, 0, 0] => [...]
[0, 0, 1]


Navie approach: iterate through all triplets. O(N^3)

[-1,0,1,2,-1,-4]
[-6, 4, 2, 0]
  ^i    ^j

HashMap approach O(N^2)
preprocess: (value) -> last index
for i idx:
    for j idx:
        complement = -1 * (value at i + value at j)
        search if complement exist.
        if complement exist, is the last occurance of complement after j.
        sort triplet, insert into result
deduplication for triplets.
Con: we need to deduplicate. We need to check indexes.

Idea #2, sorted array: O(N^2 log N)
[-2,-1,-6,3,4,2]
Sorted:
[-6,-2,-1,2,3,4]

[0,2,4,5,-5,-2,-1]
Sorted:
[-5,-2,-1,0,2,4,5]

Generate all pairs
Then search complement in the right, no index duplication.
Early stopping possible (does not impact big O).

Index deduplication !=- triplet deduplication

[0, 0, 0]


[-6, 4, 2, 0]
-6: 0
4: 1
2: 2
0: 3
[0, 1, 1]
[0, 0, 0]
0: 2

[-1,0,1,2,-1,-4]
-1: 4
0: 1
1: 2
2: 3
-4: 5
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # value => last index
        numMap = dict()
        for i, num in enumerate(nums):
            numMap[num] = i

        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = 0 - nums[i] - nums[j]
                if complement not in numMap:
                    continue

                if numMap[complement] <= j:
                    continue

                result.add(tuple(sorted((nums[i], nums[j], complement))))

        # deduplicate
        result = list(result)
        return result
