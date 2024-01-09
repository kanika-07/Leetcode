#15. 3Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
"""
Time: O(n^2)
Space: O(∣ans∣)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                    while nums[r] == nums[r+1] and l<r:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans
"""
Sample
Input
nums = [-1,0,1,2,-1,-4]
Output
[[-1,-1,2],[-1,0,1]]
"""
