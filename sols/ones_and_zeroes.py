class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        
        def count(s):
            return [s.count("0"), s.count("1")]
        
        for zero, one in [count(s) for s in strs]:
            for i in xrange(m, -1, -1):
                for j in xrange(n, -1, -1):
                    if zero <= i and one <= j:
                        dp[i][j] = max(dp[i-zero][j-one] + 1, dp[i][j])
        
        return dp[m][n]