#11. Container With Most Water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

"""
Time: O(1)
Space: O(1)
"""

class Solution(object):
    """
    maxArea calculates the maximum area of water that can be held between vertical lines represented by an array. 
    It uses a two-pointer approach, starting from the outermost lines and gradually moving inward. 
    At each step, it calculates the area formed by the two lines and keeps track of the maximum area found so far. 
    The method continues this process until the two pointers converge, returning the maximum area of water that can be contained between the lines.
    """
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            shorter_line = min(height[left], height[right])
            max_area = max(max_area, shorter_line*(right - left))
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return max_area
    
