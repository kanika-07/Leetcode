# 383. Ransom Note
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""
"""
Time: O(∣ransomNote∣+∣magazine∣)
Space: O(26)=O(1)
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count1 = collections.Counter(ransomNote)
        count2 = collections.Counter(magazine)
        return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
"""
Sample
Input
ransomNote = "a"
magazine = "b"
Output
false
"""
