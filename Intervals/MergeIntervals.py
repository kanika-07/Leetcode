# 56. Merge Intervals
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
"""
Time: O(sort)
Space: O(n)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals):
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
"""
Input
intervals = [[1,3],[2,6],[8,10],[15,18]]
Output
[[1,6],[8,10],[15,18]]
"""
