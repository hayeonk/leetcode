from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        C = Counter()
        for domain in cpdomains:
            n, s = domain.split()
            n = int(n)
            domainList = s.split(".")
            for i in xrange(len(domainList)):
                C[".".join(domainList[i:])] += n
        
        ans = []
        for domain in C:
            cp = "%d %s" % (C[domain], domain)
            ans.append(cp)
        return ans