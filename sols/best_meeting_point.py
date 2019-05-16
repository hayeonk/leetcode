class Solution(object):
    def minTotalDistance(self, grid):
        if not grid or not grid[0]:
            return 0
        
        x = []
        y = []
        n = len(grid)
        m = len(grid[0])
        
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        
        if not x:
            return 0
    
        x.sort()
        y.sort()
        
        idx = len(x) / 2
        dist = sum([abs(x[i] - x[idx]) for i in xrange(len(x))]) + sum([abs(y[i] - y[idx]) for i in xrange(len(x))])
        return dist