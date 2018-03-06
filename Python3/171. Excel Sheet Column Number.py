class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        chardict = dict(zip(string.ascii_uppercase, range(1, 27)))
        sum = 0
        factor = 1
        for char in s[::-1]:
            sum += chardict[char] * factor
            factor *= 26
        return sum
