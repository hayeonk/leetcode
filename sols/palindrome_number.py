class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        lo, hi = 0, len(x)-1
        while lo <= hi:
            if x[lo] != x[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True