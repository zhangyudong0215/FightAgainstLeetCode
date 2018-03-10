# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next: # 44ms
        #     return head
        # a, b, c = None, head, head.next
        # while c:
        #     b.next = a
        #     a, b, c = b, c, c.next
        # b.next = a
        # return b
            
        if not head: # 48ms
            return head
        prev, node = None, head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev
