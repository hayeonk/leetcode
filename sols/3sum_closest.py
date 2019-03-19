class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        minSum = 987654321
        
        for i in xrange(n-2):
            if i == 0 or (i >= 1 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = n - 1
                while lo < hi:
                    val = nums[i] + nums[lo] + nums[hi]
                    if abs(minSum - target) > abs(val - target):
                        minSum = val
                    if val == target:
                        return target
                    elif val < target:
                        lo += 1
                    else:
                        hi -= 1
        return minSum