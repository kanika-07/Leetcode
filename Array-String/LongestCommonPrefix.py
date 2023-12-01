#14. Longest Common Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
"""
Time: O(∣strs[0]∣⋅∣strs∣)
Space: O(∣strs[0]∣)
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ""
        if strs is None or (len(strs) == 0):
            return s
        minimumLength = len(strs[0])
        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))
        for i in range(0, minimumLength):
            current = strs[0][i]
            for j in range (0, len(strs)):
                if strs[j][i] != current:
                    return s
            s += current
        return s 
