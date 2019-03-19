class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        
        n = len(nums)
        nums.sort()
        ret = []
        
        for i in xrange(n-2):
            if i == 0 or (i >= 1 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = n - 1
                val = -nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == val:
                        ret.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[lo] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < val:
                        lo += 1
                    else:
                        hi -= 1
        return ret