class Solution(object):
    def findPeakElement(self, nums):
        nums.insert(0, -9876543210)
        nums.append(-9876543210)
        
        lo = 1
        hi = len(nums)-2
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid-1
            elif nums[mid-1] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0