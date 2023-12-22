# 49. Group Anagrams
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
"""
Time: O(nklog⁡k), where n=∣strs∣ and k=∣strs[i]∣
Space: O(nk)
"""
class Solution(object):
    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)
        return dict.values()
"""
Sample
Input
strs = ["eat","tea","tan","ate","nat","bat"]
Output
[["tan","nat"],["bat"],["eat","tea","ate"]]
Expected
[["bat"],["nat","tan"],["ate","eat","tea"]]
"""
