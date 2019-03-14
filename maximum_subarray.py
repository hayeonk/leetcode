class Solution(object):
    def maxSubArray(self, nums):
        ret = nums[0]
        for i in xrange(1, len(nums)):
                nums[i] = max(nums[i-1]+nums[i], nums[i])
                ret = max(ret, nums[i])
        return ret