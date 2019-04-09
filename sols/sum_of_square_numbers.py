class Solution(object):
    def judgeSquareSum(self, c):
        def isSquare(n):
            lo, hi = 0, n
            while lo <= hi:
                mid = (lo + hi) / 2
                if mid * mid == n:
                    return True
                elif mid * mid < n:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False
        
        for i in xrange(c + 1):
            if i * i > c:
                break
            if isSquare(c - i * i):
                return True
        return False