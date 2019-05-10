class Solution(object):
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        count = [[0] * m for _ in xrange(n)]
        
        def calculate(i, j):
            count[i][j] += 1
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                while 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != "W":
                    count[ni][nj] += 1
                    ni, nj = ni + di, nj + dj
            
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == "E":
                    calculate(i, j)
                    
        return max([0] + [count[i][j] for i in xrange(n) for j in xrange(m) if grid[i][j] == "0"])