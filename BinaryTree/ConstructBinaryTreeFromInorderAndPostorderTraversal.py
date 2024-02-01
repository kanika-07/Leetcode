# 106. Construct Binary Tree from Inorder and Postorder Traversal
"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inToIndex = {num: i for i, num in enumerate(inorder)}
        
        def build(inStart: int, inEnd: int, postStart: int, postEnd: int) -> Optional[TreeNode]:
            if inStart > inEnd:
                return None
            rootVal = postorder[postEnd]
            rootInIndex = inToIndex[rootVal]
            leftSize = rootInIndex - inStart
            root = TreeNode(rootVal)
            root.left = build(inStart, rootInIndex - 1, postStart, postStart + leftSize - 1)
            root.right = build(rootInIndex + 1, inEnd, postStart + leftSize, postEnd - 1)
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
"""
Sample 
Input
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Output
[3,9,20,null,null,15,7]
"""
