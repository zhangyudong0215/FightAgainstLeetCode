class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numsDict = collections.Counter(numbers) # 60ms 但是这个方法没有使用到升序的性质
        # nums = list(numsDict.keys())
        # indexDict = {}
        # for i in range(len(numbers)-1, -1, -1):
        #     indexDict[numbers[i]] = i
        # for num in nums:
        #     numsDict[num] -= 1
        #     factor = target - num
        #     if num <= factor:
        #         if factor == num and numsDict[num] > 0:
        #             return [indexDict[num]+1, indexDict[num]+2]
        #         if numsDict[factor] > 0:
        #             return [indexDict[num]+1, indexDict[factor]+1]
        #     numsDict[num] += 1
        
        left, right = 0, len(numbers)-1 # 44ms
        while left < right:
            if numbers[left] == target - numbers[right]:
                break
            elif numbers[left] > target - numbers[right]:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]
