# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        candidate = range(n)
        
        while len(candidate) >= 2:
            a = candidate.pop()
            b = candidate.pop()
            if knows(a, b):
                candidate.append(b)
            else:
                candidate.append(a)
        
        cnt = 0
        for i in xrange(n):
            if i == candidate[0]:
                continue
            if knows(i, candidate[0]):
                cnt += 1
            if knows(candidate[0], i):
                return -1
        
        return -1 if cnt < n - 1 else candidate[0]