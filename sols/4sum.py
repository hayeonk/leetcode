class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ret = []
        
        for i in xrange(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                lo = j + 1
                hi = n - 1
                val = target - nums[i] - nums[j]
                while lo < hi:
                    if nums[lo] + nums[hi] == val:
                        ret.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < val:
                        lo += 1
                    else:
                        hi -= 1
        return ret
                    