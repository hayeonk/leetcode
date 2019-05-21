from collections import defaultdict, Counter
class Solution(object):
    def numberOfPatterns(self, m, n):
        d = defaultdict(Counter)
        d[1][3] = d[3][1] = 2
        d[1][7] = d[7][1] = 4
        d[1][9] = d[9][1] = 5
        d[7][9] = d[9][7] = 8
        d[3][9] = d[9][3] = 6
        d[4][6] = d[6][4] = 5
        d[2][8] = d[8][2] = 5
        d[3][7] = d[7][3] = 5
        
        def backtrack(picked):
            if m <= len(picked) <= n:
                ans.append(picked)
            
            if len(picked) < n:
                last = picked[-1]
                for num in xrange(1, 10):
                    if num not in picked and (d[last][num] == 0 or d[last][num] in picked):
                        backtrack(picked + [num])
        
        ans = []
        for i in xrange(1, 10):
            backtrack([i])
        return len(ans)