# 30. Substring with Concatenation of All Words
"""
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
"""
"""
Time: O(∣s∣∣words∣∣words[0]∣)
Space: O(Σ∣words[i]∣)
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or words == []:
            return []
        k = len(words)
        n = len(words[0])
        ans  = []
        count = collections.Counter(words)
        for i in range(len(s) - k*n+1):
            seen = collections.defaultdict(int)
            j = 0
            while j < k:
                word = s[i+j*n : i+j*n+n]
                seen[word] += 1
                if seen[word] > count[word]:
                    break
                j += 1
            if j == k:
                ans.append(i)
        return ans
"""
Sample
Input
s = "barfoothefoobarman"
words = ["foo","bar"]
Output
[0,9]
"""
