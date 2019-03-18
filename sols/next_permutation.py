class Solution(object):
    def nextPermutation(self, nums):
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i < 0:
            reverse(0, len(nums)-1)
        else:
            for j in reversed(xrange(i+1, len(nums))):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
            reverse(i+1, len(nums)-1)