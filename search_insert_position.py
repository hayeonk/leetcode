class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo