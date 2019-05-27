class Solution(object):
    def numMagicSquaresInside(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        def magic(a, b, c, d, e, f, g, h, i):
            return sorted([a, b, c, d, e, f, g, h, i]) == range(1, 10) and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15)
        
        ans = 0
        for i in xrange(n-2):
            for j in xrange(m-2):
                if grid[i+1][j+1] != 5:
                    continue
                if magic(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]):
                    ans += 1
        return ans