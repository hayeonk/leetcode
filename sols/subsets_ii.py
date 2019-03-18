class Solution(object):
    def subsetsWithDup(self, nums):
        ret = []
        n = len(nums)
        nums.sort()
        used = [False] * n
        
        def backtrack(picked, cur):
            ret.append(picked)
            for i in xrange(cur + 1, n):
                if used[i]: 
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                backtrack(picked + [nums[i]], i)
                used[i] = False
                
        backtrack([], -1)
        return ret