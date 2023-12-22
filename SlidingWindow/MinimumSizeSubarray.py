#209. Minimum Size Subarray Sum
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0 # initialize left pointer to 0
        curr_sum = 0 # initialize current sum to 0
        min_len = float("inf") # initialize minimum length of subarray to positive infinity
        for right in range(len(nums)):
            curr_sum += nums[right]  # add current element to current sum
            while curr_sum >= target: # check if current sum is greater than or equal to s
                min_len = min(min_len, right - left + 1) # update minimum length of subarray
                curr_sum -= nums[left] # remove element from current sum
                left += 1 # move left pointer to the right
        return min_len if min_len != float("inf") else 0 # return minimum length of subarray or 0 if not found
"""
Sample
Input
target = 7
nums = [2,3,1,2,4,3]
Output
2
Expected
2
"""
