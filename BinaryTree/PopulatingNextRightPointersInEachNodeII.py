# 117. Populating Next Right Pointers in Each Node II
"""
Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
"""
"""
Time: O(n)
Space: O(1)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root # node that is above the current needling   
        while node:
            dummy = Node(0)# a dummy node before needling
            # Needle the children of the node
            needle = dummy
            while node:
                if node.left: # Needle the left child
                    needle.next = node.left
                    needle = needle.next
                if node.right: # Needle the right childe
                    needle.next = node.right
                    needle = needle.next
                node = node.next
            node = dummy.next # Move the node to the next level
        return root
"""
Sample
Input
[1,2,3,4,5,null,7]
Output
[1,#,2,3,#,4,5,7,#]
"""
