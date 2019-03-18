class Solution(object):
    def hammingDistance(self, x, y):
        n = x ^ y
        ret = 0
        while n > 0:
            n &= n - 1
            ret += 1
        return ret