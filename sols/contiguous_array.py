class Solution(object):
    def findMaxLength(self, nums):
        cnt = 0
        d = {}
        ans = 0
        d[0] = -1
        for i in xrange(len(nums)):
            cnt += 1 if nums[i] == 1 else -1
            if cnt in d:
                ans = max(ans, i - d[cnt])
            else:
                d[cnt] = i
                
        return ans