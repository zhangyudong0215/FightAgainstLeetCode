class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        charDict = collections.Counter(s)
        for num in charDict.values():
            count += (num // 2)*2
        return count+1 if count < len(s) else count
