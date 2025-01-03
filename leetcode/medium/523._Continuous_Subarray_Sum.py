'''
Link to problem: https://leetcode.com/problems/continuous-subarray-sum/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - Prefix sum + compartmentalize (aka hashing)
Difficulty: Medium
'''

'''
For k = 6

example 1:

[1,2,3]
 ^___^
Sum = 6

example 2:

[6,1,2]
 ^ (length = 1)
False

[6,0,2]
 ^_^
Sum = 6

example 3:

[4,1,2,3]
   ^___^
Sum = 6

example 4:

[12,3,6,2,4,7]
      ^___^

normalize:
[0,3,0,2,4,1]

Sum:
[0,3,3,5,9,10]

okay we can see here that 9-3=6.

Future normalizing this doesn't seem to help, seem to provide false-potivies.
[0,3,3,5,3,4]

Is normalization actually needed? Sum without normalization:
[12,15,21,23,27,34]
We could still see 27-21=6 here, normalization not needed

Let's see this provided example:
[23,2,6,4,7]
 ^________^ sum=42

Sum:
[23,25,31,35,42]
we can see 42-0 is a multiple of 6, not a good example.

Slightly modify:
[1,23,2,6,4,7]
   ^________^ sum=42

Sum:
[1,24,26,32,36,43]
we can see 43-1 is a multiple of 6.

Next question, how do we standing at 43 search for 1,7,13,19,...
This search would still be O(N), meaning total complexity is O(N^2)

To reduce big-o we have these options:
O(N log N) search is O(log N), imply binary search
O(N) search is O(1), imply hashmap

I don't think normalization works here by itself:
Normalized subarray sum:
[1,0,2,2,0,1]

(after hint by looking at editorial's title)

okay we can make this easier to lookup, I was almost there.
Compartment the subarray sum by % k with key of the index.
And we shoud just record the first index.
'''

'''
Bruteforce O(N^2)

Of course timeout, good place to understand the question though.
Establishes that we will have to at least go through the entire array.
'''
class BruteForce:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for left in range(len(nums)):
            for right in range(left + 2, len(nums) + 1):
                # print(nums[left:right])
                if sum(nums[left:right]) % k == 0:
                    return True
        return False

'''
Prefix sum + compartmental solution mentioned above
O(N)

Something else I did not cover is:
[23,6,9]

normalized accumlative sum: [5,5,2]
when looking at 6, 23 (also at 5) is not a good choice
This happens when we have a single k value (not enough for subarray).
I think this could just be done with an extra check.
'''
class Optimized_1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        accumlative_sum = [nums[0]]
        for num in nums[1:]:
            accumlative_sum.append(accumlative_sum[-1] + num)
        normalized_sums = [num % k for num in accumlative_sum]

        # This table cannot be a dict, k is maybe too big
        normalized_table = dict()
        normalized_table[0] = 0
        for idx, normalized_sum in enumerate(normalized_sums):
            if normalized_sum not in normalized_table:
                # we take the first index
                normalized_table[normalized_sum] = idx

        for right_idx, num in enumerate(normalized_sums):
            if num not in normalized_table:
                continue
            left_idx = normalized_table[num]
            if right_idx == left_idx:
                continue
            # we have k value (s), since there's only two values,
            # we can check do a direct check
            # (if both are k, this is a valid subarray)
            if right_idx == left_idx + 1:
                if (nums[right_idx] + nums[left_idx]) % k != 0:
                    continue
            return True

        return False

'''
We can definitly see there's more room for improvement.
We can simply merge some loops here.
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        normalized_table = dict()

        prev_sum = 0
        for right_idx, num in enumerate(nums):
            prev_sum += num
            normalized_sum = prev_sum % k

            if normalized_sum == 0:
                # first element is k
                if right_idx == 0:
                    continue
                # sum of array[:right_idx+1] is multiple of k
                return True

            if normalized_sum not in normalized_table:
                normalized_table[normalized_sum] = right_idx
                continue

            left_idx = normalized_table[normalized_sum]
            # there's a index in [left, right] pointing to a k multiple
            if right_idx == left_idx + 1:
                if (nums[right_idx] + nums[left_idx]) % k != 0:
                    continue

            return True

        return False
