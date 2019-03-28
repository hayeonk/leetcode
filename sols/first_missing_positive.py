class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in xrange(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                idx = nums[i] - 1
                nums[idx], nums[i] = nums[i], nums[idx]
                
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return max(1, n+1)