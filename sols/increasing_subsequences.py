class Solution(object):
    def findSubsequences(self, nums):
        ret = {}
        
        def dfs(picked, idx):
            if len(picked) >= 2:
                ret[tuple(picked)] = 1
            
            for i in xrange(idx, len(nums)):
                if not picked or nums[i] >= picked[-1]:
                    dfs(picked + [nums[i]], i + 1)
        dfs([], 0)
        ans = []
        for picked in ret:
            ans.append(list(picked))
        return ret