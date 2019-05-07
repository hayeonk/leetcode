class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(1, len(nums)):
            if i % 2 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            if i % 2 == 0 and nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]