class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        ret = [1] * n
        for i in xrange(1, n):
            for j in reversed(xrange(i)):
                if nums[j] < nums[i]:
                    ret[i] = max(ret[i], ret[j] + 1)
            
        return max(ret)