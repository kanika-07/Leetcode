#2. Add Two Numbers

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum_value = carry
            if l1 is not None:
                sum_value = sum_value + l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value = sum_value + l2.val
                l2 = l2.next
            node = ListNode(sum_value % 10)
            carry = sum_value // 10
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        
        if carry > 0:
            temp.next = ListNode(carry)
        return head