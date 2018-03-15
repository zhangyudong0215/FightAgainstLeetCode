class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        index = [0] * len(S) # 50ms 左右
        indexDict = {}
        for i, char in enumerate(S):
            if char in indexDict:
                indexDict[char][1] = i
            else:
                indexDict[char] = [i, i]
        for slices in indexDict.values():
            index[slices[0]: slices[1]] = [1] * (slices[1] - slices[0])
        ans = []
        last = 0
        for i, num in enumerate(index):
            if num == 0:
                ans.append(i+1-last)
                last = i + 1
        return ans
