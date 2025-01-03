# Link to problem: https://leetcode.com/problems/accounts-merge/
# Loom explaining solution you wrote (5m): 
# Solution:
# Description
# Key ideas
# This is a distinct graph/ union find question
# Difficulty: Easy
# Code

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = dict()
        for idx, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email not in emailMap:
                    emailMap[email] = list()
                emailMap[email].append(idx)

        res = []
        visited_email = set()
        for start in emailMap.keys():
            if start in visited_email:
                continue

            name = accounts[emailMap[start][0]][0]

            emails = set()
            visited_idx = set()
            q = [start]
            while q:
                cur = q[-1]
                q.pop()

                assert cur not in visited_email

                if cur in emails:
                    continue
                else:
                    emails.add(cur)

                for idx in emailMap[cur]:
                    # Optimization
                    if idx in visited_idx:
                        continue
                    else:
                        visited_idx.add(idx)

                    for email in accounts[idx][1:]:
                        q.append(email)

            visited_email = visited_email | emails
            res.append([name] + sorted(emails))

        return res


