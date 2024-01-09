# 290. Word Pattern
"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        t = s.split()
        return[map(pattern.index, pattern)] == [map(t.index, t)]
"""
Sample
Input
pattern = "abba"
s = "dog cat cat dog"
Output
true
"""
