#58. Length of Last Word
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = len(s) - 1 
        while ind >= 0 and s[ind] == " ":
            ind -= 1
        lastIndex = ind
        while ind >= 0 and s[ind] != " ":
            ind -= 1
        return lastIndex - ind
"""
Sample
Input
s = "Hello World"
Output
5
"""
