class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in xrange(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
            
        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]