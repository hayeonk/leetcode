from collections import defaultdict
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        d = defaultdict(list)
        d[0].append(-1)
        
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            d[cur].append(i)
            
        ans = 0
        for n in d:
            if n + k in d:
                l1 = d[n]
                l2 = d[n + k]
                ans = max(ans, l2[-1] - l1[0])
        return ans