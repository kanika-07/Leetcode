#3. Longest Substring Without Repeating Characters

"""Given a string s, find the length of the longest substring without repeating characters."""

"""
Time: O(n)
Space:O(1)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res = 0
        for i in range(n):
            visited = [0] * 256
            for j in range(i,n):
                if (visited[ord(s[j])] == True):
                    break
                else:
                    res = max(res, j-i+1)
                    visited [ord(s[j])] = True
            visited[ord(s[i])] = False
        return res
