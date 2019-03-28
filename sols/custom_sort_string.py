from collections import Counter

class Solution(object):
    def customSortString(self, S, T):
        ret = []
        T = Counter(T)
        for i in xrange(len(S)):
            if T[S[i]] != 0:
                ret += [S[i]] * T[S[i]]
                T[S[i]] = 0
        for t in T:
            if T[t] != 0:
                ret += [t] * T[t]
        return "".join(ret)