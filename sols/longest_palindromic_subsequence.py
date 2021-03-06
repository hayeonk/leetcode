class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in xrange(n)]
        
        for i in xrange(n):
            dp[i][i] = 1
        
        for i in reversed(xrange(n)):
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]