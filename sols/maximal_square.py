class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        ans = 0
        for i, row in enumerate(matrix):
            matrix[i] = list(map(int, row))
            if any(matrix[i]):
                ans = 1
            
        n = len(matrix)
        m = len(matrix[0])
        for i in xrange(1, n):
            for j in xrange(1, m):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
                    ans = max(ans, matrix[i][j]**2)
        return ans