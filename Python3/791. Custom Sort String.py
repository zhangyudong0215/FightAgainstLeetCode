class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # ruleDict = dict(zip(list(S), range(len(S)))) # 156ms 思路是构造新的比较规则, 然后利用排序算法排序
        # def bigger(a, b):
        #     if a in ruleDict and b in ruleDict and ruleDict[a] < ruleDict[b]:
        #         return False
        #     else:
        #         return True # 只要有一个其它字母都交换顺序
        # T = list(T)
        # for i in range(len(T)-1, 0, -1): # 冒泡排序
        #     for j in range(i):
        #         if bigger(T[j], T[j+1]):
        #             T[j], T[j+1] = T[j+1], T[j]
        # return ''.join(T)
        
        # ans = [] # 44ms 思路是统计字母次数
        # charCountDict = collections.Counter(T)
        # for char in S:
        #     if char in charCountDict:
        #         ans.extend([char]*charCountDict[char])
        #         del charCountDict[char]
        # for char in charCountDict:
        #     ans.extend([char]*charCountDict[char])
        # return ''.join(ans)
        
        ans = [] # 40ms 修改的统计输出
        charCountDict = collections.Counter(T)
        for char in S:
            if char in charCountDict:
                ans.extend([char for i in range(charCountDict[char])])
                del charCountDict[char]
        for char in charCountDict:
            ans.extend([char for i in range(charCountDict[char])])
        return ''.join(ans)
