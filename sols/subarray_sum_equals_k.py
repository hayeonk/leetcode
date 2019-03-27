from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        n = len(nums)
        d = defaultdict(int)
        d[0] += 1
        curSum = 0
        for i in xrange(n):
            curSum += nums[i]
            ans += d[curSum - k]
            d[curSum] += 1
        return ans