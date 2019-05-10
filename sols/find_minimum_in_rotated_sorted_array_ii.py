class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]