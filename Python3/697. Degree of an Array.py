class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # numsDict = {} # 108ms
        # indexDict = {}
        # for index, num in enumerate(nums):
        #     numsDict[num] = numsDict.get(num, 0) + 1
        #     if num not in indexDict:
        #         indexDict[num] = [index]
        #     else:
        #         indexDict[num].append(index)
        # maxcount = max(numsDict.values())
        # length = []
        # for num in numsDict:
        #     if numsDict[num] == maxcount:
        #         length.append(indexDict[num])
        # ans = length[0][-1] - length[0][0] + 1
        # for item in length:
        #     ans = min(ans, item[-1] - item[0] + 1)
        # return ans
        
        numsDict = {} # 80ms
        indexDict = {}
        for index, num in enumerate(nums):
            if num not in numsDict:
                numsDict[num] = 1
                indexDict[num] = [index, index]
            else:
                numsDict[num] += 1
                indexDict[num][-1] = index
        maxcount = max(numsDict.values())
        minlength = 50001
        for num in indexDict:
            if numsDict[num] == maxcount:
                length = indexDict[num][-1] - indexDict[num][0] + 1
                if length < minlength: 
                    minlength = length
        return minlength
