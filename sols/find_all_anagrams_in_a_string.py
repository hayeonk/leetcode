from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        
        pdict = defaultdict(int)
        for c in p:
            pdict[c] += 1
        
        n = len(p)
        sdict = defaultdict(int)
        for c in s[:n]:
            sdict[c] += 1
        
        ret = [0] if pdict == sdict else []
        for i in xrange(n, len(s)):
            sdict[s[i]] += 1
            sdict[s[i-n]] -= 1
            if sdict[s[i-n]] == 0:
                del sdict[s[i-n]]
            if pdict == sdict:
                ret.append(i-n+1)
        return ret