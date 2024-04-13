# 1151. Minimum Swaps to Group All 1's Together
"""
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
"""
"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = data.count(1)
        ones = 0 # the number of ones in the window
        maxOnes = 0 # the maximum number of ones in the window
        for i, num in enumerate(data):
            if i>=k and data[i-k]:
                ones -= 1
            if num:
                ones += 1
            maxOnes = max(maxOnes, ones)
        return k - maxOnes
"""
Input
data = [1,0,1,0,1]
Output
1
"""
