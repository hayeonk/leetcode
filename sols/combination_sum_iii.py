from math import factorial

class Solution(object):
    def combinationSum3(self, k, n):
        def backtrack(picked, curIdx, k, n):
            if k == 0:
                if n == 0:
                    ret.append(picked)
                return
            
            for i in xrange(curIdx, 10):
                if i <= n:
                    backtrack(picked + [i], i+1, k-1, n-i)
        
        if factorial(9) / factorial(9 - k) < n:
            return []
        
        ret = []
        backtrack([], 1, k, n)
        return ret