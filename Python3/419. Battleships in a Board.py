class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # r = len(board)
        # c = len(board[0])
        # def remove(i, j):
        #     board[i][j] = '.'
        #     if i > 0 and board[i-1][j] == 'X': remove(i-1, j)
        #     if i < r - 1 and board[i+1][j] == 'X': remove(i+1, j)
        #     if j > 0 and board[i][j-1] == 'X': remove(i, j-1)
        #     if j < c - 1 and board[i][j+1] == 'X': remove(i, j+1)
        # ans = 0
        # for i in range(r):
        #     for j in range(c):
        #         if board[i][j] == 'X':
        #             ans += 1
        #             remove(i, j)
        # return ans
        
        ans = 0 # 44ms
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 只有左和上不是'X'才记录一次
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                    ans += 1
        return ans