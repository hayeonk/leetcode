class Solution(object):
    def maxA(self, N):
        dp = [0] * (N + 1)
        dp[1] = 1
        
        for i in xrange(2, N + 1):
            dp[i] = dp[i-1] + 1
            for k in xrange(2, i):
                dp[i] = max(dp[i], dp[i-k] * (k-1))
        return dp[N]