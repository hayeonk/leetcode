class Solution(object):
    def findJudge(self, N, trust):
        candidate = set(range(1, N+1))
        for a, b in trust:
            candidate.discard(a)
        if not candidate or len(candidate) > 1:
            return -1
        
        check = set()
        for a, b in trust:
            if b in candidate:
                check.add(a)
        if len(check) == N-1:
            return list(candidate)[0]
        return -1