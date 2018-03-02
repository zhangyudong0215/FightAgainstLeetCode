class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
#         r = len(matrix)
#         c = len(matrix[0])
        
#         isToeplitz = True

#         for i in range(len(matrix)-1):
#             string1 = ''.join(map(str, matrix[i][:c-1]))
#             string2 = ''.join(map(str, matrix[i+1][1:]))
#             if string1 != string2:
#                 isToeplitz = False

#         return isToeplitz

        return all(row1[:-1] == row2[1:] for row1, row2 in zip(matrix[:-1], matrix[1:])) # 最快，个人认为也是最好的方法

        # nums = {}
        # for i, row in enumerate(matrix):
        #     for j, value in enumerate(row):
        #         if i-j not in nums:
        #             nums[i-j] = value
        #         elif value != nums[i-j]:
        #             return False
        # return True
