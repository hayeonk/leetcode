class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        
        xor &= -xor
        ret = [0, 0]
        for i in nums:
            if i & xor:
                ret[0] ^= i
            else:
                ret[1] ^= i
        return ret