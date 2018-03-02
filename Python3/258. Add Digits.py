class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 关键在于Go中 -1%9 = -1 而python3中 -1%9 = -8
        return (num-1)%9 + 1 if num > 0 else 0 # 64ms, 其他的方法没什么意思
