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
        i = 0
        sum1 = 0
        while True:
            sum1 += l1.val*pow(10, i)
            if l1.next:
                l1 = l1.next
                i += 1
            else:
                break
        i = 0
        sum2 = 0
        while True:
            sum2 += l2.val*pow(10, i)
            if l2.next:
                l2 = l2.next
                i += 1
            else:
                break
        sum3 = sum1 + sum2
        list3 = []
        while True:
            list3.append(sum3%10)
            if not sum3//10:
                break
            else:
                sum3 = sum3//10
        nodelist = []
        for num in list3:
            nodelist.append(ListNode(num))
        for i in range(len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        return nodelist[0]
