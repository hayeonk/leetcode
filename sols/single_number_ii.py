class Solution(object):
    def singleNumber(self, nums):
        x1 = x2 = 0
        for n in nums:
            x2 ^= n & x1
            x1 ^= n
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1