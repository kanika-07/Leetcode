# 2297. Jump Game VIII
"""
You are given a 0-indexed integer array nums of length n. You are initially standing at index 0. You can jump from index i to index j where i < j if:
    nums[i] <= nums[j] and nums[k] < nums[i] for all indexes k in the range i < k < j, or
    nums[i] > nums[j] and nums[k] >= nums[i] for all indexes k in the range i < k < j.
You are also given an integer array costs of length n where costs[i] denotes the cost of jumping to index i.
Return the minimum cost to jump to the index n - 1.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # dp[i] := the minimum cost to jump to i
        dp = [math.inf] * len(nums)
        maxStack = []
        minStack = []

        dp[0] = 0
        
        for i, num in enumerate(nums):
            while maxStack and num >= nums[maxStack[-1]]:
                dp[i] = min(dp[i], dp[maxStack.pop()] + costs[i])
            while minStack and num < nums[minStack[-1]]:
                dp[i] = min(dp[i], dp[minStack.pop()] + costs[i])
            maxStack.append(i)
            minStack.append(i)
        return dp[-1]
"""
Input
nums = [3,2,4,4,1]
costs = [3,7,6,4,2]
Output
8
"""
