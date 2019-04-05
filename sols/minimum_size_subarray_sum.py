class Solution(object):
    def minSubArrayLen(self, s, nums):
        start = 0
        minLen = float('inf')
        curSum = 0
        for i in xrange(len(nums)):
            curSum += nums[i]
            while curSum >= s:
                minLen = min(minLen, i - start + 1)
                curSum -= nums[start]
                start += 1
                
        return 0 if minLen == float('inf') else minLen