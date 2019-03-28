class Solution(object):
    def countPrimes(self, n):
        if n <= 1:
            return 0
        
        A = [1] * n
        for i in xrange(2, int(n**0.5)+1):
            for j in xrange(i*i, n, i):
                A[j] = 0
                
        return A[2:].count(1)