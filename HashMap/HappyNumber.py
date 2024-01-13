# 202. Happy Number
"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
"""
Time: O(log⁡n)
Space: O(1)
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def squaredSum(n):
            total = 0
            while n:
                total += pow(n % 10, 2)
                n //= 10
            return total

        slow = squaredSum(n)
        fast = squaredSum(squaredSum(n))

        while slow != fast:
            slow = squaredSum(slow)
            fast = squaredSum(squaredSum(fast))
        return slow == 1
"""
Sample 
Input
n = 19
Output
true
"""
