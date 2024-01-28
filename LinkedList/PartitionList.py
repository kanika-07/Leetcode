# 86. Partition List
"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeHead = ListNode(0)
        afterHead = ListNode(0)
        before = beforeHead
        after = afterHead
        while head:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next
        after.next = None
        before.next = afterHead.next
        return beforeHead.next
"""
Sample
Input
head = [1,4,3,2,5,2]
x = 3
Output
[1,2,2,4,3,5]
"""
