from bisect import bisect_left
class Solution(object):
    def shortestToChar(self, S, C):
        n = len(S)
        index = [i for i in xrange(n) if S[i] == C]
        ans = [-1] * n
        
        for i in xrange(n):
            idx = bisect_left(index, i)
            if idx == len(index):
                ans[i] = i - index[-1]
            else:
                ans[i] = min(abs(i - index[idx]), abs(i - index[idx-1]))
        
        return ans