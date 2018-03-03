class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # if set(s) != set(t): # 40ms
        #     return list(set(t)-set(s))[0]
        # sDict = {}
        # tDict = {}
        # for char in set(s):
        #     sDict[char] = 0
        #     tDict[char] = 0
        # for char1 in s:
        #     sDict[char1] += 1
        # for char2 in t:
        #     tDict[char2] += 1
        # for char in set(s):
        #     if tDict[char] > sDict[char]:
        #         return char
        
        # # 用看起来厉害一点的写法重写上面的代码 就需要44ms了
        # if set(s) != set(t):
        #     return (set(t) - set(s)).pop()
        # charDict = {}
        # for char in t:
        #     charDict.setdefault(char, 0)
        #     charDict[char] += 1
        # for char in s:
        #     charDict[char] -= 1
        # for key in set(s):
        #     if charDict.pop(key) == 1:
        #         return key
        
        # return [i for i in t if i not in s or s.count(i) != t.count(i)][0] # 76ms
        
        # ans = 0 # 44ms 位运算，需要ord函数和chr函数的支持，其他语言执行起来可能有难度
        # for c in s + t:
        #     ans ^= ord(c)
        # return chr(ans)
        
        hashtable = [0] * 26 # 48ms
        for i in range(len(s)):
            hashtable[ord(s[i]) - 97] -= 1
            hashtable[ord(t[i]) - 97] += 1
        hashtable[ord(t[-1]) - 97] += 1
        i = 0
        for i in range(26):
            if hashtable[i]:
                break
        return chr(i + 97)
