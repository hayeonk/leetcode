class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        
        n = len(nums)
        dp = [[x] for x in nums]
        nums.sort()
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max((dp[i], dp[j] + [nums[i]]), key=len)
        
        return max(dp, key=len)