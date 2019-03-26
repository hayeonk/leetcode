class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for _ in xrange(n)]
        ans = n
        
        for i in xrange(n):
            if i > 0 and s[i] == s[i-1]:
                dp [i-1][i] = 1
                ans += 1
            dp[i][i] = 1
            
        for i in reversed(xrange(n)):
            for j in xrange(i+2, n):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]:
                    ans += 1
        
        return ans