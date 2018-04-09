class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordDict = {} # 位运算, elegant的想法
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            wordDict[mask] = max(wordDict.get(mask, 0), len(word))
        ans = 0
        for mask1, mask2 in itertools.combinations(wordDict.keys(), 2):
            if not (mask1 & mask2):
                ans = max(ans, wordDict[mask1] * wordDict[mask2])
        return ans
