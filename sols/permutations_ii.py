class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return nums
        
        nums.sort()
        n = len(nums)
        ret = []
        used = [False] * n
        def backtrack(picked):
            if len(picked) == n:
                ret.append(picked)
            else:
                for i in xrange(n):
                    if used[i]: 
                        continue
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    backtrack(picked + [nums[i]])
                    used[i] = False
                
        backtrack([])
        return ret