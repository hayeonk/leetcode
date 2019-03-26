class Solution(object):
    def moveZeroes(self, nums):
        idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
                
        for i in xrange(idx, len(nums)):
            nums[i] = 0