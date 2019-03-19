class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        
        ret = 1
        cur = 1
        for i in xrange(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += 1
                ret = max(ret, cur)
            else:
                cur = 1
        return ret