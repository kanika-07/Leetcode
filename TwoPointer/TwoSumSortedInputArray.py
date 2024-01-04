# 167. Two Sum II - Input Array Is Sorted
"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_ind = 0
        right_ind = len(numbers) - 1
        while left_ind < right_ind:
            total = numbers[left_ind] + numbers[right_ind]
            if total == target:
                return [left_ind+1, right_ind+1]
            if total < target:
                left_ind += 1
            else:
                right_ind -= 1
"""
Input
numbers = [2,7,11,15]
target = 9
Output
[1,2]
"""
