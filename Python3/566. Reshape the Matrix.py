class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        num1D = [x for row in nums for x in row]
        if len(nums)*len(nums[0]) != r*c or len(nums) == r:
            return nums
        else:
            return [num1D[i*c:i*c+c] for i in range(r)]
