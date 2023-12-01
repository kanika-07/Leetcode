# LeetCode 27. Remove Element
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
"""

"""
Time: O(n)
Space: O(1)
"""

class Solution(object):
    """
     removeElement modifies an array of integers in-place to remove all occurrences of a specific value. 
     It iterates through the array, replacing occurrences of the specified value with the following non-matching elements. 
     It also keeps track of the count of non-matching elements and returns this count, representing the new length of the modified array without the specified value.
     """
    def removeElement(self, nums, val):
        count = 0
        for i  in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
