class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid-1] >= nums[mid]:
                return nums[mid]
            if nums[mid] >= nums[(mid+1)%n]:
                return nums[(mid+1)%n]
            if nums[lo] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[lo]