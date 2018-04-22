class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexs = [i for i in range(len(S)) if S[i] == C]
        ans = []
        for i in range(len(S)):
            length = len(S)
            for index in indexs:
                length = min(length, abs(i-index))
            ans.append(length)
        return ans
