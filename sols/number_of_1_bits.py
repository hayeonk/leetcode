class Solution(object):
    def hammingWeight(self, n):
        ret = 0
        while n > 0:
            ret += 1
            n = n & (n-1)
        return ret