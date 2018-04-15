class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = ''.join([c for c in paragraph if ord(c)>=97 and ord(c)<=122 or c == ' '])
        wordlist = [w for w in paragraph.split(' ') if w]
        wordDict = collections.Counter(wordlist).most_common()
        i = 0
        while True:
            if wordDict[i][0] in banned:
                i += 1
            else:
                return wordDict[i][0]
