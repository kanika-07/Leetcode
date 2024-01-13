# 219. Contains Duplicate II
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        for i, num in enumerate(nums):
            if i>k:
                seen.remove(nums[i-k-1])
            if num in seen:
                return True
            seen.add(num)
        return False
"""
Sample
Input
nums = [1,2,3,1]
k = 3
Output
true
"""
