# 274. H-Index
"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
"""
Time: O(sort)
Space: O(1)
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        for i, citation in enumerate(citations):
            if citation >= n-i:
                return n-i
        return 0
"""
Sample
Input
citations = [3,0,6,1,5]
Output
3
"""
