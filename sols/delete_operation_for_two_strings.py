class Solution(object):
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        n = len(word1)
        m = len(word2)
        
        if n == 1:
            return m - 1 if word1[0] in word2 else m + 1
        if m == 1:
            return n - 1 if word2[0] in word1 else n + 1
        
        dp = [[0] * m for _ in xrange(n)]
        maxVal = 0
        
        for i in xrange(n):
            for j in xrange(m):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 if i == 0 or j == 0 else dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                maxVal = max(maxVal, dp[i][j])
        
        return n + m - 2 * maxVal