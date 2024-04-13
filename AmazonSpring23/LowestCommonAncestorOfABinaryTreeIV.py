# 1676. Lowest Common Ancestor of a Binary Tree IV
"""
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.
"""
"""
Time: O(n)
Space: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def lca(root: 'TreeNode')->'TreeNode':
            if not root:
                return None
            if root in nodes:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if left and right:
                return root
            return left or right
        return lca(root)
"""
Input
[3,5,1,6,2,0,8,null,null,7,4]
[4,7]
Output
2
"""
