# 101. Symmetric Tree
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
"""
Time: O(n)
Space: O(h)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
            if not p or not q:
                return p == q
            return p.val == q.val and isSymmetric(p.left, q.right) and isSymmetric(p.right, q.left)
        return isSymmetric(root, root)       
"""
Sample
Input
root = [1,2,2,3,4,4,3]
Output
true
"""
