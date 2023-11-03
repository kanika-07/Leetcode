# 21. Merge Two Sorted Lists

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
"""
Time: O(∣list1∣+∣list2∣))
Space: O(∣list1∣+∣list2∣))
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        while list1 is not None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
        return head