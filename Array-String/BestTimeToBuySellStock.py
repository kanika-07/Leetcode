#121. Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    left_ptr, profit = 0, 0
    for right_ptr in range(1, len(prices)):
      if prices[left_ptr] < prices[right_ptr]:
        profit = max(profit, prices[right_ptr] - prices[left_ptr])
      else:
        left_ptr = right_ptr
    return profit

"""
Sample
Input
prices = [7,1,5,3,6,4]
Output
5
Expected
5
"""
