class Solution(object):
    def __init__(self):
        self.ans = 0
    def countArrangement(self, N):
        def backtrack(picked):
            if len(picked) == N:
                self.ans += 1
                return
            
            n = len(picked) + 1
            
            for i in xrange(1, N+1):
                if i in picked:
                    continue
                if i % n == 0 or n % i == 0:
                    backtrack(picked + [i])
        
        backtrack([])
        return self.ans