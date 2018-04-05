# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1 or not l2: # 224ms
        #     return l1 if l1 else l2
        # stack1 = []
        # stack2 = []
        # while l1:
        #     stack1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     stack2.append(l2.val)
        #     l2 = l2.next
        # ans = None
        # a = 0
        # while len(stack1) > 0 and len(stack2) > 0:
        #     val = stack1.pop() + stack2.pop() + a
        #     a = val // 10
        #     b = val % 10
        #     temp = ListNode(b)
        #     temp.next = ans
        #     ans = temp
        # stack = stack1 if len(stack1) > 0 else stack2
        # while len(stack) > 0:
        #     val = stack.pop() + a
        #     a = val // 10
        #     b = val % 10
        #     temp = ListNode(b)
        #     temp.next = ans
        #     ans = temp
        # if a > 0:
        #     temp = ListNode(a)
        #     temp.next = ans
        #     ans = temp
        # return ans
        
        stackl1 = [] # 128ms
        stackl2 = []
        total = 0
        cur = ListNode(0)
        while l1:
            stackl1.append(l1.val)
            l1 = l1.next
        while l2:
            stackl2.append(l2.val)
            l2 = l2.next
        while stackl1 or stackl2:
            if stackl1:
                total += stackl1.pop()
            if stackl2:
                total += stackl2.pop()
            cur.val = total % 10
            total //= 10
            head = ListNode(total)
            head.next = cur
            cur = head
        return cur.next if cur.val == 0 else cur
