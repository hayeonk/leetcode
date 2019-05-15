class Solution(object):
    def __init__(self):
        self.d = {}
    def integerReplacement(self, n):
        if n == 1:
            return 0
        
        if n%2 == 0:
            return 1 + self.integerReplacement(n/2)
        
        if n in self.d:
            return self.d[n]
        
        self.d[n] = 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        return self.d[n]