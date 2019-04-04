class Solution(object):
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        dp = [0] * n
        ans = 0
        
        for i in xrange(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
                ans += dp[i]
        return ans