# 1431. Kids With the Greatest Number of Candies
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
"""
"""
Time: O(1)
Space: O(1)
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return [candy + extraCandies >= maxCandy for candy in candies]
"""
Sample
Input
candies = [2,3,5,1,3]
extraCandies = 3
Output
[true,true,true,false,true]
"""
