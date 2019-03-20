class Solution(object):
    def search(self, nums, target):
        def binSearch(target):
            lo = 0
            hi = len(nums)-1
            while lo <= hi:
                mid = (lo + hi) / 2
                if nums[mid] == target:
                    return True
                if nums[lo] < nums[mid]:
                    if nums[lo] <= target and target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < nums[lo]:
                    if nums[mid] < target and target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                else:
                    lo += 1
            return False
        if not nums:
            return False
        return binSearch(target)