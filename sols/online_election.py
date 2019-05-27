from collections import Counter
from bisect import *
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.times = times
        self.candidate = []
        
        C = Counter()
        R = Counter()
        for vote in persons:
            C[vote] += 1
            R[C[vote]] = vote
            maxVote = max(C.values())
            self.candidate.append(R[maxVote])
        
    def q(self, t):
        idx = bisect_right(self.times, t) - 1
        return self.candidate[idx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)