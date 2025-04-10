"""
Loom: https://www.loom.com/share/af46138b6b1d4697aba240226c4e2155

[[10,20],[30,200],[400,50],[30,20]]
A: [0, 1]
B: [2, 3]


[[10,20],[30,200],[400,50],[30,50]]
A: [1, 3]
B: [2, 0]

[[10, 20], [10, 20], [10, 20], [10, 20]]
A: [1,2]
B: [3,4]

[[10, 20], [10, 20], [110, 120], [110, 120]]
A: [1,2] => 20     [3,4] => 220
B: [3,4] => 240    [1,2] => 40

Idea:
1. spread everybody to their minimal cost city. O(N)
2. equalize the number of people (aka. move overflow to another city). O(N log N)
    people with minimal moving cost first by sorting.
3. compute the total cost.

"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # [[10,20],[30,200],[400,50],[30,50]]
        aList = []  # 1 3 ovf
        bList = []  # 2 0

        for i, (aCost, bCost) in enumerate(costs):
            if aCost < bCost:
                aList.append(i)
            else:
                bList.append(i)

        if len(aList) > len(bList):
            overflowingList = aList
            receivingList = bList
        else:
            overflowingList = bList
            receivingList = aList

        # lower moving cost, higher index.
        overflowingList.sort(key=lambda idx: -abs(costs[idx][0] - costs[idx][1]))
        while len(overflowingList) != len(receivingList):
            receivingList.append(overflowingList[-1])
            overflowingList.pop()
        
        result = 0
        for idx in aList:
            result += costs[idx][0]
        for idx in bList:
            result += costs[idx][1]
        return result
