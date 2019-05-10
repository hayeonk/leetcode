class Solution(object):
    def __init__(self):
        self.m = {}
    def numDistinct(self, s, t):
        if not s or not t:
            return 0
        
        if len(t) == 1:
            return s.count(t)
        
        if (s, t) in self.m:
            return self.m[(s, t)]
        
        ans = 0
        for i in xrange(len(s)):
            if s[i] == t[0]:
                ans += self.numDistinct(s[i+1:], t[1:])
        self.m[(s, t)] = ans
        return ans