# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi) / 2
            ret = guess(mid)
            if ret == 0:
                return mid
            elif ret > 0:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo