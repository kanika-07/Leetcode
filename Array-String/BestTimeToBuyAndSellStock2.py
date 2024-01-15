# 122. Best Time to Buy and Sell Stock II
"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""
"""
Time = O(n)
Space = O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mx = 0
        n = len(prices)
        for i in reversed(range(1, n)):
            mx = max(mx, prices[i]-prices[i-1]+mx)
        return mxv
"""
Sample
Input
prices = [7,1,5,3,6,4]
Output
7
"""
