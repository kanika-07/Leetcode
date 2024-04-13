# 1492. The kth Factor of n
"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""
"""
Time: O(root(n))
Space: O(1)
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = 1
        i = 0  # the i-th factor

        while factor < int(math.sqrt(n)):
            if n % factor == 0:
                i += 1
                if i == k:
                    return factor
            factor += 1

        factor = n // factor
        while factor >= 1:
            if n % factor == 0:
                i += 1
                if i == k:
                    return n // factor
            factor -= 1
        return -1
"""
Sample 
Input
n = 12
k = 3
Output
3
"""
