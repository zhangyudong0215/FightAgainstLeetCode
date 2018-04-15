# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # nums = [] # 超时
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        # ans = 0
        # count = 0
        # for num in nums:
        #     if num in G:
        #         count += 1
        #     else:
        #         if count > 0:
        #             ans += 1
        #             count = 0
        # if nums[-1] in G:
        #     ans += 1
        # return ans
        
        # ans = 0 # 超时
        # count = 0
        # if head.val in G:
        #     count += 1
        # while head.next:
        #     head = head.next
        #     if head.val in G:
        #         count += 1
        #     else:
        #         if count > 0:
        #             ans += 1
        #             count = 0
        # if head.val in G:
        #     ans += 1
        # return ans
        
        nums = []
        numsOrder = {}
        i = 0
        while head:
            nums.append(head.val)
            numsOrder[head.val] = i
            i += 1
            head = head.next
        cuts = list(set(nums) - set(G))
        ans = ['0'] * i
        for num in cuts:
            ans[numsOrder[num]] = '1'
        return len([x for x in ''.join(ans).split('1') if x])
