class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        candidates.sort()
        def backtrack(picked, target, k):
            if target < 0:
                return
            if target == 0:
                ret.append(picked)
            else:
                for i in xrange(k + 1, len(candidates)):
                    if i != k + 1 and candidates[i] == candidates[i-1]: 
                        continue
                    backtrack(picked + [candidates[i]], target - candidates[i], i)
        backtrack([], target, -1)
        
        return ret