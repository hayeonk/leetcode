class Solution(object):
    def permute(self, nums):
        if not nums:
            return nums
        
        n = len(nums)
        ret = []
        def backtrack(picked):
            if len(picked) == n:
                ret.append(picked)
            else:
                for i in nums:
                    if i not in picked:
                        backtrack(picked + [i])
        backtrack([])
        return ret