class Solution(object):
    def multiply(self, A, B):
        n = len(A)
        m = len(A[0])
        t = len(B[0])
        
        ans = [[0] * t for _ in xrange(n)]
        
        for i in xrange(n):
            for j in xrange(t):
                add = 0
                for k in xrange(m):
                    add += A[i][k] * B[k][j]
                ans[i][j] = add
        return ans