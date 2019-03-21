class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        minV = maxV = ret = nums[0]
        
        for i in xrange(1, n):
            if nums[i] < 0:
                minV, maxV = maxV, minV
            
            maxV = max(nums[i], maxV * nums[i])
            minV = min(nums[i], minV * nums[i])
            
            ret = max(ret, maxV)
        return ret