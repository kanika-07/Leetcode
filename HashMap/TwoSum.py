#1. Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
Time: O(n)
Space: O(n)
"""

class Solution(object):
    """
    twoSum finds two numbers in an array whose sum matches a given target. It uses a dictionary to store previously seen numbers and their indices while iterating 
    through the array. For each number, it checks if the difference between the target and the current number (remaining) is in the dictionary. 
    If found, it returns the indices of the two numbers that add up to the target.
    """
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]
            
            seen[value] = i
