class Solution(object):
    def removeElement(self, nums, val):
        nextIdx = -1
        for i in xrange(len(nums)):
            if nums[i] != val:
                nextIdx += 1
                nums[nextIdx] = nums[i]
        return nextIdx + 1
        