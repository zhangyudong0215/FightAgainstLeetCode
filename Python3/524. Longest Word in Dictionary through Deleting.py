class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # def match(word): # 排序会异常得慢
        #     i = j = 0
        #     while i < len(s) and j < len(word):
        #         if s[i] == word[j]:
        #             j += 1
        #         i += 1
        #     return j == len(word)
        # d.sort(key=lambda x: (-len(x), x))
        # for word in d:
        #     if match(word):
        #         return word
        # return ''
        
        # def match(word): # 一样慢
        #     i = j = 0
        #     while i < len(s) and j < len(word):
        #         if s[i] == word[j]:
        #             j += 1
        #         i += 1
        #     return j == len(word)
        # ans = ''
        # for word in d:
        #     if match(word):
        #         if len(word) > len(ans):
        #             ans = word
        #         elif len(word) == len(ans) and word < ans:
        #             ans = word
        # return ans
        
        # result = '' # 就很快, 76ms
        # for word in d:
        #     lo = 0
        #     for l in word:
        #         lo = s.find(l, lo) + 1
        #         if lo == 0:
        #             break
        #     if lo > 0 and len(word) >= len(result):
        #         if len(word) == len(result):
        #             result = word if word < result else result
        #         else:
        #             result = word
        # return result
        
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x) # 这里好像是用了iter只能遍历一次的特点
        return max(sorted(filter(isSubsequence, d)) + [''], key=len)
