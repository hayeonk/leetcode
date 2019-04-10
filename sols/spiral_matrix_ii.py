class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in xrange(n)]
        num = 1
        lo, hi = 0, n-1
        
        while lo < hi:
            for j in xrange(lo, hi):
                matrix[lo][j] = num
                num += 1
            for i in xrange(lo, hi):
                matrix[i][hi] = num
                num += 1
            for j in xrange(hi, lo, -1):
                matrix[hi][j] = num
                num += 1
            for i in xrange(hi, lo, -1):
                matrix[i][lo] = num
                num += 1
            
            lo += 1
            hi -= 1
        
        if lo == hi:
            matrix[lo][hi] = num
        
        return matrix