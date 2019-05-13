class Solution(object):
    def longestLine(self, M):
        if not M or not M[0]:
            return 0
        
        n = len(M)
        m = len(M[0])
        ans = 0
        dp = [[[0, 0, 0, 0]] * m for _ in xrange(n)]
        
        for i in xrange(n):
            for j in xrange(m):
                if M[i][j] == 1:
                    dp[i][j] = [1] * 4
                    if i > 0 and j > 0:
                        dp[i][j][2] = dp[i-1][j-1][2] + 1
                    if i > 0:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    if j > 0:
                        dp[i][j][1] = dp[i][j-1][1] + 1
                    if i > 0 and j < m - 1:
                        dp[i][j][3] = dp[i-1][j+1][3] + 1
                ans = max(ans, max(dp[i][j]))
        
        return ans