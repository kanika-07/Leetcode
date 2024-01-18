# 42. Trapping Rain Water
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]
        while left < right:
            if maxL < maxR:
                ans += maxL - height[left]
                left += 1
                maxL = max(maxL, height[left])
            else:
                ans += maxR - height[right]
                right -= 1
                maxR = max(maxR, height[right])
        return ans
"""
Sample
Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output
6
"""
