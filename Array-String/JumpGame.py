# 55. Jump Game
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return i == len(nums)        
"""
Sample
Input
nums = [2,3,1,1,4]
Output
true
"""
