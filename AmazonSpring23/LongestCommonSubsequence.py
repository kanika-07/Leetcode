# 1143. Longest Common Subsequence
"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""
"""
Time: O(mn)
Space: O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[i][j] := the length of LCS(text1[0..i], text2[0..j])
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = 1 + dp[i][j] if text1[i] == text2[j] else max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]
"""
Sample 
Input
text1 = "abcde"
text2 = "ace"
Output
3
"""
