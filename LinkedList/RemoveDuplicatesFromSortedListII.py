# 82. Remove Duplicates from Sorted List II
"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head:
                prev = prev.next
            else:
                prev.next = head.next
            head = head.next
        return dummy.next
"""
Sample
Input
head = [1,2,3,3,4,4,5]
Output
[1,2,5]
"""
