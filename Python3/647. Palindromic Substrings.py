class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) # 136ms
        ans = 0
        for center in range(2*length-1):
            left = center // 2
            right = left + center%2
            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
