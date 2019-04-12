from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        nums = Counter(nums)
        ans = 0
        for n in nums:
            if n - 1 in nums:
                ans = max(ans, nums[n-1] + nums[n])
        return ans