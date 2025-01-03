'''
Link to problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Loom explaining solution you wrote (5m):
Solution:
Description
Key ideas:
 - This is trivially, a stack question.
Difficulty: Easy
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        prev_repetitions = []

        for current_char in s:
            if not prev_repetitions or current_char != prev_repetitions[-1][0]:
                prev_repetitions.append((current_char, 1))
                continue

            new_count = prev_repetitions[-1][1] + 1
            if new_count == k:
                prev_repetitions.pop()
            else:
                prev_repetitions[-1] = current_char, new_count

        return "".join([char * count for (char, count) in prev_repetitions])
