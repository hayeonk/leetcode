import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        if n <= 1:
            return n
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        r = []
        for env in envelopes:
            pos = bisect.bisect_left(r, env[1])
            if pos == len(r):
                r.append(env[1])
            elif env[1] < r[pos]:
                r[pos] = env[1]
            
        return len(r)