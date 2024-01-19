# 19. Remove Nth Node From End of List
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
"""
Sample
Input
head = [1,2,3,4,5]
n = 2
Output
[1,2,3,5]
"""
