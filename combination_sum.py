class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        def backtrack(picked, target, k):
            if target < 0:
                return
            if target == 0:
                ret.append(picked)
			else:
				for i in xrange(k, len(candidates)):
					backtrack(picked + [candidates[i]], target - candidates[i], i)
        backtrack([], target, 0)
        return ret
        