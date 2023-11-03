#28. Find the Index of the First Occurrence in a String

"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

"""
Time: O((m-n)n) where m=haystack and n=needle
Space: O(1)
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return -1
        if haystack == needle:
            return 0
        needleLength = len(needle)
        for i in range(len(haystack) - needleLength + 1):
            if haystack[i:i + needleLength] == needle:
                return i
        return -1