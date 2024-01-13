# 128. Longest Consecutive Sequence
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        seen = set(nums)
        for num in nums:
            if num - 1 in seen:
                continue
            length = 0
            while num in seen:
                num += 1
                length += 1
            ans = max(ans, length)
        return ans        
"""
Sample
Input
nums = [100,4,200,1,3,2]
Output
4
"""
