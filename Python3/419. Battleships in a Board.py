class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r = len(board) # 48ms
        c = len(board[0])
        def remove(i, j):
            board[i][j] = '.'
            if i > 0 and board[i-1][j] == 'X': remove(i-1, j)
            if i < r - 1 and board[i+1][j] == 'X': remove(i+1, j)
            if j > 0 and board[i][j-1] == 'X': remove(i, j-1)
            if j < c - 1 and board[i][j+1] == 'X': remove(i, j+1)
        ans = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X':
                    ans += 1
                    remove(i, j)
        return ans
