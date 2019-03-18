class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
                
        if nums[lo] != target:
            return [-1, -1]
        
        ret = [lo]
        hi = len(nums)-1
        while lo < hi:
            mid = (lo + hi + 1) / 2
            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid - 1
        ret += [hi]
        return ret