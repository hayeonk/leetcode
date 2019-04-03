class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        
        j = 0
        for i in xrange(len(s)):
            if j >= len(t):
                return False
            while j < len(t) and t[j] != s[i]:
                j += 1
            j += 1
        
        return j <= len(t)