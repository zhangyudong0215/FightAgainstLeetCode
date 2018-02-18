import re

class Solution:
#     def findWords(self, words): # 使用set的第一种方法
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         new_words = []
#         for word in words:
#             if self.isOneLineWord(word):
#                 new_words.append(word)
#         return new_words
    
#     def isOneLineWord(self, word):
#         set1 = set('qwertyuiop')
#         set2 = set('asdfghjkl')
#         set3 = set('zxcvbnm')
#         word_set = set(word.lower())
#         if word_set.issubset(set1) or word_set.issubset(set2) or word_set.issubset(set3):
#             return True
#         else:
#             return False

    # def findWords(self, words): # 使用set的第二种方法
    #     """
    #     :type words: List[str]
    #     :rtype: List[str]
    #     """
    #     a=set('qwertyuiop')
    #     b=set('asdfghjkl')
    #     c=set('zxcvbnm')
    #     ans=[]
    #     for word in words:
    #         w = set(word.lower())
    #         if a&w == w or b&w == w or c&w == w:
    #             ans.append(word)
    #     return ans   

    def findWords(self, words): # 使用正则
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rx = re.compile('(^[qwertyuiop]*$|^[asdfghjkl]*$|^[zxcvbnm]*$)')
        for word in words:
            w = rx.match(word.lower())
            if w:
                ans.append(w)
        return ans

        # return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words) 
        # 参考discuss中的回答 疑问：需要小写化嘛？
