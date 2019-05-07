class Solution(object):
    def findMaxAverage(self, nums, k):
        nums = map(float, nums)
        curSum = sum(nums[:k])
        ans = curSum / k
        
        for i in xrange(k, len(nums)):
            curSum += nums[i] - nums[i-k]
            ans = max(ans, curSum / k)
        return ans