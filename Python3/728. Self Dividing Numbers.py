class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numlist = []
        for num in range(left, right+1):
            request = True
            for digit in str(num):
                if digit == '0' or num%int(digit):
                    request = False
            if request:
                numlist.append(num)
        return numlist
        # 精彩至极的python一行列表推导式
        # return [x for x in range(left, right+1) if all(y and not x%y for y in map(int,str(x)))]
