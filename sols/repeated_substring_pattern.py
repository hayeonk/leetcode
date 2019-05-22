class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        if n <= 1:
            return False
        
        for i in xrange(1, int(n**0.5)+1):
            if n % i == 0:
                if s[:i] * (n/i) == s:
                    return True
                if i != 1 and s[:n/i] * i == s:
                    return True
        return False