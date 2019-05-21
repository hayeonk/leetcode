from collections import defaultdict
from bisect import *
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        maxProfit = defaultdict(int)
        P = 0
        for d, p in sorted(zip(difficulty, profit)):
            P = max(P, p)
            maxProfit[d] = max(maxProfit[d], P)
        
        difficulty = sorted(maxProfit)
        ans = 0
        for ability in worker:
            idx = bisect_right(difficulty, ability)
            if idx == 0:
                continue
            ans += maxProfit[difficulty[idx-1]]
        return ans