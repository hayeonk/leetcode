class Solution(object):
    def canWin(self, s):
        if "++" not in s:
            return False
        
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++" and not self.canWin(s[:i] + "--" + s[i+2:]):
                return True
        return False