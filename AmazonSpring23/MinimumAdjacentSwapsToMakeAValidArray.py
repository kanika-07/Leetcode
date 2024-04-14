#2340. Minimum Adjacent Swaps to Make a Valid Array
"""
You are given a 0-indexed integer array nums.
Swaps of adjacent elements are able to be performed on nums.
A valid array meets the following conditions:
    The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
    The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minIndex = self._getLeftmostMinIndex(nums)
        maxIndex = self._getRightmostMaxIndex(nums)
        swaps = minIndex + (len(nums) - 1 - maxIndex)
        return swaps if minIndex <= maxIndex else swaps - 1
    
    def _getLeftmostMinIndex(self, nums:List[int]) -> int:
        min = nums[0]
        minIndex = 0
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
                minIndex = i
        return minIndex
    
    def _getRightmostMaxIndex(self, nums: List[int]) -> int:
        max = nums[-1]
        maxIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max:
                max = nums[i]
                maxIndex = i
        return maxIndex
"""
Sample
Input
nums = [3,4,5,5,3,1]
Output
6
"""
