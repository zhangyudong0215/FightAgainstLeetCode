class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # charDict = {} # 字典检查两个字符串 # 96ms
        # for char in s:
        #     charDict[char] = charDict.get(char, 0) + 1
        # for char in t:
        #     if char not in charDict:
        #         return False
        #     else:
        #         charDict[char] -= 1
        # for value in charDict.values():
        #     if value:
        #         return False
        # return True
        
        # return sorted(s) == sorted(t) # 80ms
        
        # 稍微修改一下字典方法 # 76ms
        if len(s) != len(t): return False
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        dict1.subtract(dict2)
        for value in dict1.values():
            if value:
                return False
        return True
