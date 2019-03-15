class Solution(object):
    def combine(self, n, k):
        ret = []
        nums = range(1, n + 1)
        def backtrack(picked, cur):
            if len(picked) == k:
                ret.append(picked)
            else:
                for i in xrange(cur + 1, n):
                    backtrack(picked + [nums[i]], i)
        backtrack([], -1)
        return ret