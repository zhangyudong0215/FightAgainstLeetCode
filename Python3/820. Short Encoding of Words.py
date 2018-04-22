class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x: len(x), reverse=True)
        ans = 0
        s = ''
        for word in words:
            if not word+'#' in s:
                ans += len(word) + 1
                s += word + '#'
        return ans
