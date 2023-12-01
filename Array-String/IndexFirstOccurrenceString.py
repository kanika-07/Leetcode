#28. Find the Index of the First Occurrence in a String

"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

"""
Time: O((m-n)n) where m=haystack and n=needle
Space: O(1)
"""

class Solution(object):
    """
    strStr finds the starting index of the first occurrence of a smaller string (needle) within a larger string (haystack). 
    It uses a simple iteration to check if needle matches a substring of the same length in haystack. If found, it returns the index where the match begins; 
    otherwise, it returns -1.
    """
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
