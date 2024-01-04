# 76. Minimum Window Substring
"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""
"""
Time: O(m+n)
Space: O(128)=O(1)
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = collections.Counter(t)
        required = len(t)
        bestLeft = -1
        minLength = len(s) + 1
        left = 0
        for right, center in enumerate(s):
            count[center] -= 1
            if count[center] >= 0:
                required -= 1
            while required == 0:
                if right - left + 1 < minLength:
                    bestLeft = left
                    minLength = right - left + 1
                count[s[left]] += 1
                if count[s[left]] > 0:
                    required += 1
                left += 1
        return '' if bestLeft == -1 else s[bestLeft: bestLeft + minLength]
  """
Sample
Input
s = "ADOBECODEBANC"
t = "ABC"
Output
"BANC"
"""
