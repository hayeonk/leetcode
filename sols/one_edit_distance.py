class Solution(object):
    def isOneEditDistance(self, s, t):
        if len(s) == len(t):
            diff = 0
            for c1, c2 in zip(s, t):
                if c1 != c2:
                    diff += 1
            return diff == 1
        
        elif abs(len(s) - len(t)) == 1:
            if len(s) < len(t):
                s, t = t, s
            
            for i in xrange(len(s)):
                if s[:i] + s[i+1:] == t:
                    return True
            return False
            
        else:
            return False