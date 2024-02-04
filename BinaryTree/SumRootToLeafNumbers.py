# 129. Sum Root to Leaf Numbers
"""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(root: Optional[TreeNode], path:int) -> None:
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans += path * 10 + root.val
                return
            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)
        dfs(root, 0)
        return ans
"""
Sample
Input
root = [1,2,3]
Output
25
"""
