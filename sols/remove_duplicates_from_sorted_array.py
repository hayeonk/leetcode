class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        nextIdx = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[nextIdx]:
                nextIdx += 1
                nums[nextIdx] = nums[i]
        return nextIdx + 1
        