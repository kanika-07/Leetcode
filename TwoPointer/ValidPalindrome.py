#125. Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
"""
Sample
Input
s = "A man, a plan, a canal: Panama"
Output
true
Expected
true
"""
