class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def isrotatedDigits(s):
            if '3' in s or '4' in s or '7' in s:
                return False
            elif '2' not in s and '5' not in s and '6' not in s and '9' not in s:
                return False
            else:
                return True
        count = 0
        for s in map(str, range(1, N+1)):
            if isrotatedDigits(s):
                count += 1
        return count
