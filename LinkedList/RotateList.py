# 61. Rotate List
"""
Given the head of a linked list, rotate the list to the right by k places.
"""
"""
Time: O(n)
Space: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head # Circle the list
        t = length - k % length
        for _ in range(t):
            tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead
"""
Sample
Input
head = [1,2,3,4,5]
k = 2
Output
[4,5,1,2,3]
"""
