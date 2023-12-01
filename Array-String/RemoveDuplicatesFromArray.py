#26. Remove Duplicates from Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

"""
Time: O(n)
Space: O(n)
"""

class Solution(object):
    """
    removeDuplicates modifies an array of sorted integers in-place to keep only unique elements. It iterates through the array, checking each element against the previous one.
    If the current element is different from the previous one, it updates the array in-place to store that unique element and keeps track of the count of unique elements.
    Finally, it returns the count of unique elements in the modified array.
    """
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
