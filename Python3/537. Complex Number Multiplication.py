class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alist = a.split('+')
        blist = b.split('+')
        aa, ab = int(alist[0]), int(alist[1][: -1])
        ba, bb = int(blist[0]), int(blist[1][: -1])
        return str(aa*ba - ab*bb) + '+' + str(aa*bb + ab*ba) + 'i'
