class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # lens = len(s) # 188ms, 很奇怪, 我觉得这个方法很好, 但是很慢
        # lent = len(t)
        # i = j = 0
        # while i < lens and j < lent:
        #     if s[i] == t[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return i == lens
        
        # if len(s) > len(t): # AC中最快的答案
        #     return False
        # for i in s:
        #     if i in t: # 额外的循环, 其实寻找了两次(第一次)
        #         index = t.find(i) # 额外的循环, 其实寻找了两次(第二次)
        #         t = t[index + 1:]
        #     else:
        #         return False
        # return True
        
        for i in s: # 事件复杂度应该和第一种方法一致才对, 为何这种方法快了那么多?
            index = t.find(i)
            if index == -1:
                return False
            else:
                t = t[index+1: ]
        return True
