# 92. Reverse Linked List II
"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""
"""
Time: O(n)
Space: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
    
    def reverseN(self, head: Optional[ListNode], n:int) -> Optional[ListNode]:
        if n == 1:
            return head
        newHead = self.reverseN(head.next, n-1)
        headNext = head.next
        head.next = headNext.next
        headNext.next = head
        return newHead
"""
Sample
Input
head = [1,2,3,4,5]
left = 2
right = 4
Output
[1,4,3,2,5]
"""
