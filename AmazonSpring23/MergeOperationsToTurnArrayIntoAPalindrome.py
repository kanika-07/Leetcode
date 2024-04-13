# 2422. Merge Operations to Turn Array Into a Palindrome
"""
You are given an array nums consisting of positive integers.
You can perform the following operation on the array any number of times:
    Choose any two adjacent elements and replace them with their sum.
        For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = len(nums) - 1
        leftSum = nums[0]
        rightSum = nums[-1]

        while l < r:
            if leftSum < rightSum:
                l += 1
                leftSum += nums[l]
                ans += 1
            elif leftSum > rightSum:
                r -= 1
                rightSum += nums[r]
                ans += 1
            else: # leftSum == rightSum
                l += 1
                r -= 1
                leftSum = nums[l]
                rightSum = nums[r]
        return ans
"""
Input
nums = [4,3,2,1,2,3,1]
Output
2
"""
