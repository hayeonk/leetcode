class Solution(object):
    def numSquares(self, n):
        dp = [987654321] * (n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in xrange(2, n+1):
            for j in xrange(1, i):
                if j * j <= i:
                    dp[i] = min(dp[i], 1 + dp[i - j * j])
                else:
                    break
        
        return dp[n]