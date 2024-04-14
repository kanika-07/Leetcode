# 2330. Valid Palindrome IV
"""
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.
Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def makePalindrome(self, s: str) -> bool:
        change = 0
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] != s[r]:
                change += 1
                if change > 2:
                    return False
            l+=1
            r-=1
        return True
"""
Sample
Input
s = "abcdba"
Output
true
"""
