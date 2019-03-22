class Solution(object):
    def trailingZeroes(self, n):
        cnt = 0
        i = 5
        while n / i > 0:
            cnt += n / i
            i *= 5
        return cnt