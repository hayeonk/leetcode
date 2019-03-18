class Solution(object):
    def sortColors(self, nums):
        if not nums:
            return nums
        
        i, first, end = 0, 0, len(nums)-1
        while i <= end:
            if nums[i] == 0 and first != i:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
            elif nums[i] == 2 and end != i:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1
        