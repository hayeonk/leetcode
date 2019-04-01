class Solution(object):
    def __init__(self):
        self.m = {}
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1 / x, -n)
        
        if n == 0:
            return 1
        
        if (x, n) in self.m:
            return self.m[(x, n)]
        if n % 2 == 1:
            self.m[(x, n)] = x * self.myPow(x, n / 2) * self.myPow(x, n / 2)
            return self.m[(x, n)]
        else: 
            self.m[(x, n)] = self.myPow(x, n / 2) * self.myPow(x, n / 2)
            return self.m[(x, n)]