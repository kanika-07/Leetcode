# 2405. Optimal Partition of String
"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        used = 0
        for c in s:
            i = ord(c) - ord('a')
            if used >> i & 1:
                used = 1 << i
                ans += 1
            else:
                used |= 1 << i
        return ans
"""
Sample
Input
s = "abacaba"
Output
4
"""
