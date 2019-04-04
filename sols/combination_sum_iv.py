class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        for n in nums:
            if n <= target:
                dp[n] = 1
        for i in xrange(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]
        return dp[target]