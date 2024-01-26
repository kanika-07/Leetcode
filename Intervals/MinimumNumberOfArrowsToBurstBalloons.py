# 452. Minimum Number of Arrows to Burst Balloons
"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""
"""
Time: O(nlog⁡n)
Space: O(1)
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        arrowX = -math.inf
        for point in sorted(points, key = lambda x: x[1]):
            if point[0] > arrowX:
                ans += 1
                arrowX = point[1]
        
        return ans
"""
Sample
Input
points = [[10,16],[2,8],[1,6],[7,12]]
Output
2
"""
