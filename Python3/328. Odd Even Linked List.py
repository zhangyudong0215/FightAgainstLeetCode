# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odds = head
        first_odd = head
        evens = head.next
        first_even = head.next
        head = evens.next
        count = 1
        while head:
            if count == 1:
                odds.next = head
                odds = odds.next
                count = 0
            else:
                evens.next = head
                evens = evens.next
                count = 1
            head = head.next
        evens.next = None # 防止出现环
        odds.next = first_even
        return first_odd
