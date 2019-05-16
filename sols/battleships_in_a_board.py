class Solution(object):
    def countBattleships(self, board):
        n = len(board)
        m = len(board[0])
        cnt = 0 
        
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == "X" and (i==0 or board[i-1][j] == ".") and (j==0 or board[i][j-1] == "."):
                    cnt += 1
        return cnt