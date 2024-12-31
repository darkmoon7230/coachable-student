'''
Link to problem: https://leetcode.com/problems/detect-cycles-in-2d-grid/
Loom explaining solution you wrote (5m): 
Solution:
Description
Key ideas
- See below for my own solution
- Realize that the problem space is fairly defined (biggest age is 120)
Difficulty:
Medium
'''

'''
Thinking:
1. Brute force is trivial to write
2. This is a range finding question, we should sort the array first
3. Per: age[y] > age[x] we should partition by sorting so we can have a lower bound
4. Per: age[y] <= 0.5 * age[x] + 7 we gathers the upper bound of the serch space
5. Per: age[y] > 100 && age[x] < 100 we gather a specific lower bound

For the pair of (x, y) to be valid, this is the requirment:
age[y] > 0.5 * age[x] + 7
age[y] <= age[x]
age[y] <= 100 || age[x] >= 100

0.5 * age[x] + 7 < age[y] <= age[x]
age[x] < 100 => age[y] <= 100
'''

def leftMostIndexOf(arr: List[int], target: int) -> int:
    lo, high = 0, len(arr)
    while lo < high:
        mid = (high - lo) // 2 + lo
        if arr[mid] < target:
            lo = mid + 1
        else:
            high = mid
    return lo

def leftMostIndexAfter(arr: List[int], target: float) -> int:
    if target % 1 != 0:
        next_val = ceil(target)
    else:
        next_val = target + 1
    return leftMostIndexOf(arr, next_val)

class BinarySearch:

    def numFriendRequests(self, age: List[int]) -> int:
        age.sort()

        res = 0
        for x in range(len(age)):
            lower_bound_val = 0.5 * age[x] + 7

            upper_bound_val = age[x]
            if age[x] < 100:
                upper_bound_val = min(upper_bound_val, 100)
            upper_bound_val += 1

            lower_bound = leftMostIndexAfter(age, lower_bound_val)
            upper_bound = leftMostIndexOf(age, upper_bound_val)

            res += max(upper_bound - lower_bound - 1, 0)
        return res


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        counter = [0] * 121
        for age in ages:
            counter[age] += 1

        res = 0
        for x_age in ages:
            smallest_valid = 0.5 * x_age + 7
            if smallest_valid % 1 != 0:
                smallest_valid = ceil(smallest_valid)
            else:
                smallest_valid = int(smallest_valid) + 1

            for y_age in range(smallest_valid, x_age):
                if y_age > 100 and x_age < 100:
                    continue
                res += counter[y_age]
            res += counter[x_age] - 1
        return res
