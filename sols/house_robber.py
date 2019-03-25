class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        steal = nums[0]
        not_steal = 0
        
        for i in xrange(1, n):
            steal, not_steal = nums[i] + not_steal, max(steal, not_steal)
        return max(steal, not_steal)