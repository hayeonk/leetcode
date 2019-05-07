from collections import Counter
class Solution(object):
    def generatePalindromes(self, s):
        C = Counter(s)
        
        if sum([1 for x in C if C[x] % 2]) > 1:
            return []
        
        halfChr = []
        middle = ""
        
        for x in C:
            if C[x] % 2:
                middle = x
            halfChr += [x] * (C[x] / 2)
        
        halfChr.sort()
        ans = []
        
        def makePermutation(picked, pickFrom):
            if not pickFrom:
                ans.append(picked + middle + picked[::-1])
                return
            
            for i in xrange(len(pickFrom)):
                if i > 0 and pickFrom[i-1] == pickFrom[i]:
                    continue
                makePermutation(picked + pickFrom[i], pickFrom[:i] + pickFrom[i+1:])
        
        makePermutation("", halfChr)
        return ans