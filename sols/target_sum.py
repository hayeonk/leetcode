class Solution(object):
    def __init__(self):
        self.m = {}
        
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        
        if (tuple(nums), S) in self.m:
            return self.m[(tuple(nums), S)]
        
        n = len(nums)
        if n == 1:
            if nums[0] == S and S == 0:
                ret = 2
            elif nums[0] == abs(S):
                ret = 1
            else:
                ret = 0
            self.m[(tuple(nums), S)] = ret
            return ret
            
        self.m[(tuple(nums), S)] = self.findTargetSumWays(nums[1:], S + nums[0]) + self.findTargetSumWays(nums[1:], S - nums[0])
        return self.m[(tuple(nums), S)]