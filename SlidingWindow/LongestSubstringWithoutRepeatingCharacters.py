#3. Longest Substring Without Repeating Characters

"""Given a string s, find the length of the longest substring without repeating characters."""

"""
Time: O(n)
Space:O(1)
"""

class Solution(object):
    """
    lengthOfLongestSubstring finds the length of the longest substring in a string without any repeating characters. 
    It iterates through the string and uses a sliding window approach to identify substrings without repeating characters. 
    The method keeps track of visited characters using an array and determines the length of the longest substring without repeating characters, 
    returning this length as the result.
    """
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
