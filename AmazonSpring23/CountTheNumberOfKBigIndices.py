# 2519. Count the Number of K-Big Indices
"""
You are given a 0-indexed integer array nums and a positive integer k.
We call an index i k-big if the following conditions are satisfied:
    There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
    There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
Return the number of k-big indices.
"""
"""
Time: O(nlog⁡n)
Space: O(n)
"""
class FenwickTree:
    def __init__(self, n: int):
        self.sums = [0] * (n + 1)

    def update(self, i: int, delta: int) -> None:
        while i < len(self.sums):
            self.sums[i] += delta
            i += FenwickTree.lowbit(i)

    def get(self, i: int) -> int:
        summ = 0
        while i > 0:
            summ += self.sums[i]
            i -= FenwickTree.lowbit(i)
        return summ

    @staticmethod
    def lowbit(i: int) -> int:
        return i & -i

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        leftTree = FenwickTree(n)
        rightTree = FenwickTree(n)
        # left[i] := the number of `nums` < nums[i] with index < i
        left = [0] * n
        # right[i] := the number of `nums` < nums[i] with index > i
        right = [0] * n

        for i, num in enumerate(nums):
            left[i] = leftTree.get(num - 1)
            leftTree.update(num, 1)

        for i in range(n - 1, -1, -1):
            right[i] = rightTree.get(nums[i] - 1)
            rightTree.update(nums[i], 1)

        return sum(l >= k and r >= k for l, r in zip(left, right))
"""
Input
nums = [2,3,6,5,2,3]
k = 2
Output
2
"""
