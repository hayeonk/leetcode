class Solution(object):
    def findDerangement(self, n):
        mod = 10 ** 9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in xrange(2, n + 1):
            dp[i] = (i - 1L) * (dp[i-1] + dp[i-2]) % mod
        return dp[n]