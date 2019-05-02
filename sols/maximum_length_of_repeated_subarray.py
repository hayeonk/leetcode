class Solution(object):
    def findLength(self, A, B):
        n = len(A)
        m = len(B)
        dp = [[0] * m for _ in xrange(n)]
        ans = 0
        
        for i in xrange(n):
            dp[i][0] = int(A[i] == B[0])
        for j in xrange(m):
            dp[0][j] = int(A[0] == B[j])
            
        for i in xrange(1, n):
            for j in xrange(1, m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])
        return ans