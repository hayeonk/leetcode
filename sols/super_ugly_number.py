import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        q = [1]
        d = {}
        for i in xrange(n):
            num = heapq.heappop(q)
            for p in primes:
                if num * p not in d:
                    heapq.heappush(q, num * p)
                    d[num * p] = 1
        return num