import re

class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if len(S) == 0:
            return 0

        items = []
        char = S[0]
        count = 0
        for i in range(len(S)):
            if S[i] == char:
                count += 1
            else:
                items.append((char, count))
                char = S[i]
                count = 1
        items.append((char, count))
        pattern = ''
        for char, count in items:
            if count < 3:
                pattern += char * count
            else:
                pattern += char + '{1,' + str(count) + '}'
        ans = 0
        for word in words:
            response = re.match(pattern, word)
            if response and len(word) == len(response.group()):
                ans += 1
        return ans
