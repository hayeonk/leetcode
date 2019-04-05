class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        
        ans = 0
        for i in xrange(n):
            for j in xrange(n):
                if grid[i][j]:
                    ans += 2
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < n and 0 <= nj < n:
                        nval = grid[ni][nj]
                    else:
                        nval = 0
                    ans += max(grid[i][j] - nval, 0)
        return ans