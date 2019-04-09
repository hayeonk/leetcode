class Solution(object):
    def isPerfectSquare(self, num):
        lo, hi = 0, num
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False