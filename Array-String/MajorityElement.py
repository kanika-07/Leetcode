#169. Majority Element
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    ans = None
    count = 0
    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)
    return ans
"""
Sample
Input
nums = [3,2,3]
Output
3
Expected
3
"""
