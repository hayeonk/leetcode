class Solution(object):
    def uniquePaths(self, m, n):
        board = [[0] * n for _ in xrange(m)]
        board[0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if i > 0: 
                    board[i][j] += board[i-1][j]
                if j > 0:
                    board[i][j] += board[i][j-1]
        return board[-1][-1]