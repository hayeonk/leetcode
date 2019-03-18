class Solution(object):
    def subsets(self, nums):
        ret = []
        n = len(nums)
        
        def backtrack(picked, cur):
            ret.append(picked)
            for i in xrange(cur + 1, n):
                backtrack(picked + [nums[i]], i)
        
        backtrack([], -1)
        return ret