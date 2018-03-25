class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==1: return False
        global_avg = sum(A)/float(len(A))
        for lenB in range(1, math.ceil(len(A)/2)+1):
            if int(lenB*global_avg) == lenB*global_avg:
                if self.exist(lenB*global_avg, lenB, A):
                    return True
        return False
            
    def exist(self, tosum, lenB, arr):
        if lenB==0:
            return False if tosum else True
        if lenB > len(arr) or not arr: 
            return False
        if any([self.exist(tosum-arr[0], lenB-1, arr[1:]),
               self.exist(tosum, lenB, arr[1:])]):
            return True
        return False
