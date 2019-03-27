class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        l = [1] * n
        
        for i in xrange(1, n):
            l[i] = l[i-1] * nums[i-1]
        
        p = 1
        for i in reversed(xrange(n-1)):
            p *= nums[i+1]
            l[i] *= p
        
        return l