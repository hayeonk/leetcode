class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        board = [[0] * n for _ in xrange(m)]
        board[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    board[i][j] += board[i-1][j]
                if j > 0:
                    board[i][j] += board[i][j-1]
        return board[-1][-1]