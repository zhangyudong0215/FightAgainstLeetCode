class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        ans = []
        for index, word in enumerate(S.split(' ')):
            newword = ''
            if word[0] in 'aeiouAEIOU':
                newword += word + 'ma'
            else:
                newword += word[1: ] + word[0] + 'ma'
            newword += 'a' * (index+1)
            ans.append(newword)
        return ' '.join(ans)
