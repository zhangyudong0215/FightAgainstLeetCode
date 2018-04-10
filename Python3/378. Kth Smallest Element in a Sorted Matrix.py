class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # nums = [(matrix[0][0], 0, 0)] # 超时
        # fill = matrix[0][0] - 1
        # matrix[0][0] = fill
        # ans = 0
        # r, c = len(matrix), len(matrix[0])
        # while k > 0:
        #     ans, x, y = min(nums, key=lambda x: x[0])
        #     nums.pop(nums.index((ans, x, y)))
        #     if x < r-1 and matrix[x+1][y] > fill:
        #         nums.append((matrix[x+1][y], x+1, y))
        #         matrix[x+1][y] = fill
        #     if y < c-1 and matrix[x][y+1] > fill:
        #         nums.append((matrix[x][y+1], x, y+1))
        #         matrix[x][y+1] = fill
        #     k -= 1
        # return ans
        
        # nums = [] # 68ms, 很快, 但是空间复杂度很高
        # for row in matrix:
        #     nums.extend(row)
        # return sorted(nums)[k-1]
        
        r, c = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[r-1][c-1]
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = c - 1 # 此处利用了列中的有序
            for i in range(r):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
