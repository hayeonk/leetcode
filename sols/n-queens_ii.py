class Solution(object):
    def totalNQueens(self, n):
        def backtrack(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                ret.append(1)
            for q in xrange(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens + [q], xy_diff + [p-q], xy_sum + [p+q])
        ret = []
        backtrack([], [], [])
        return len(ret)