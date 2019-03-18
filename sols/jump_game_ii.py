class Solution(object):
    def jump(self, nums):
        n = len(nums)
        i = minCnt = 0
        curMax = nextMax = 0
        
        while i < n:
            while i < n and i <= curMax:
                nextMax = max(nextMax, i + nums[i])
                i += 1
                
            minCnt += 1
            curMax = nextMax
            
        return minCnt-1