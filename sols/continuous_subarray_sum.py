from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            for i in xrange(len(nums)-1):
                if nums[i] == nums[i+1] == 0:
                    return True
            return False
        
        if len(nums) < 2:
            return False
        
        k = abs(k)
        s = defaultdict(list)
        s[0].append(-1)
        val = 0
        for i, n in enumerate(nums):
            val = (val + n) % k
            if val in s and i - s[val][0] > 1:
                return True
            s[val].append(i)
        return False