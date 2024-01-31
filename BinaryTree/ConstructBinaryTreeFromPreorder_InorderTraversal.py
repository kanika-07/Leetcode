# 105. Construct Binary Tree from Preorder and Inorder Traversal
"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
"""
Time: O(n)
Space: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inToIndex = {num: i for i, num in enumerate(inorder)}
        
        def build(preStart: int, preEnd: int, inStart: int, inEnd: int) -> Optional[TreeNode]:
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            rootInIndex = inToIndex[rootVal]
            leftSize = rootInIndex - inStart
            root = TreeNode(rootVal)
            root.left = build(preStart + 1, preStart + leftSize, inStart, rootInIndex - 1)
            root.right = build(preStart + leftSize + 1, preEnd, rootInIndex + 1, inEnd)
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
"""
Sample
Input
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Output
[3,9,20,null,null,15,7]
"""
