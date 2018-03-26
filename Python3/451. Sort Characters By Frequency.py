class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sDict = collections.Counter(s) # 80ms
        # sList = sorted(sDict.items(), key=lambda x: x[1], reverse=True)
        # return ''.join([s[0]*s[1] for s in sList])
        
        sList = collections.Counter(s).most_common() # 44ms
        ans = ''
        for s in sList:
            ans += s[0] * s[1]
        return ans
