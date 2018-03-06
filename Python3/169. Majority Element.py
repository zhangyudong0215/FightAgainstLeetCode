class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # numsDict = {}
        # threshold = math.floor(len(nums)/2)
        # for num in nums:
        #     if num not in numsDict:
        #         numsDict[num] = 1
        #     else:
        #         numsDict[num] += 1
        # for num in numsDict:
        #     if numsDict[num] > threshold:
        #         return num
        
        # 这里本来想用排序: return sorted(nums)[len(nums)//2] 
        # 但是后来发现排序这个是不对的，比如[3, 3, 3, 4, 5, 6]
        
        numsDict = collections.Counter(nums) # 这个用的也是映射，不过是collections包
        return max(numsDict.keys(), key=numsDict.get)
