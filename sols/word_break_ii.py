class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        ret = []
        f = [0] * (n + 1)
        f[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        if not f[-1]:
            return []
        
        def backtrack(picked, idx):
            if idx >= len(s):
                ret.append(" ".join(picked))
                return
            
            for j in xrange(idx+1, len(s)+1):
                if s[idx:j] in wordDict:
                    backtrack(picked + [s[idx:j]], j)
        
        backtrack([], 0)
        return ret
        