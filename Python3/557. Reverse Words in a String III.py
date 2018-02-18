class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # new_list = []
        # for string in s.split():
        #     new_list.append(string[::-1])
        # return " ".join(new_list)
        return ' '.join([i[::-1] for i in s.split(' ')])
