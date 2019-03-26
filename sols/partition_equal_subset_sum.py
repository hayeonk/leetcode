class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if len(nums) <= 1 or total % 2 == 1:
            return False
        
        m = {}
        
        def canMake(nums, val):
            if val in nums:
                return True
            if val in m:
                return m[val]
            for i, n in enumerate(nums):
                if n < val:
                    if canMake(nums[:i] + nums[i+1:], val - n):
                        m[val] = True
                        return True
            m[val] = False
            return False
        
        return canMake(nums, total/2)