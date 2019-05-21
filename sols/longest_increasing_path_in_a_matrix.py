class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        
        def dfs(i, j):
            if (i, j) in d:
                return d[(i, j)]
            
            ret = 1
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1 ,0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    ret = max(ret, 1 + dfs(ni, nj))
            d[(i, j)] = ret
            return ret
        
        d = {}
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                ans = max(ans, dfs(i, j))
        return ans