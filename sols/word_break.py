class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        for i in xrange(1, n+1):
            for j in xrange(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        
        return f[-1]