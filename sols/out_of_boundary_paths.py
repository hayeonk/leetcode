class Solution(object):
    def __init__(self):
        self.m = {}
        
    def findPaths(self, m, n, N, i, j):
        mod = 10 ** 9 + 7
        if i < 0 or j < 0 or i >= m or j >= n:
            return 1
        if N == 0:
            return 0
        if (i, j, N) in self.m:
            return self.m[(i, j, N)]
        ans = self.findPaths(m, n, N-1, i+1, j) + self.findPaths(m, n, N-1, i-1, j) + self.findPaths(m, n, N-1, i, j+1) + self.findPaths(m, n, N-1, i, j-1)
        ans %= mod
        self.m[(i, j, N)] = ans
        return ans
        
        