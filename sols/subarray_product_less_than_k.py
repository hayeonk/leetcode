class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        ret = 0
        n = len(nums)
        j = -1
        cur = 1
        for i in xrange(n):
            cur *= nums[i]
            while cur >= k:
                j += 1
                cur /= nums[j]
            ret += (i - j)
        return ret