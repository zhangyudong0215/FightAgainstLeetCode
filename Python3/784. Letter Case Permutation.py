class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
#         S = S.lower()
#         isalpha = []
#         for s in S:
#             isalpha.append(s.isalpha())

#         word_list = []
#         for i in range(pow(2, sum(isalpha))):
#             string = []
#             temp = list(bin(i|8192)[3:])
#             for index, item in enumerate(isalpha):
#                 if not item or not temp.pop() == '1':
#                     string.append(S[index])
#                 else:
#                     string.append(str(S[index]).upper())
#             word_list.append(''.join(string))
        
#         return word_list

        word_list = [''] # 最直接的方法，而且比上面这个方法还快
        for ch in S:
            if ch.isalpha():
                word_list = [i+j for i in word_list for j in [ch.lower(), ch.upper()]]
            else:
                word_list = [i+ch for i in word_list]
        return word_list
