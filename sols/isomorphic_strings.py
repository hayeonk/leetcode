class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        d = {}
        for c1, c2 in zip(s, t):
            if c1 in d and d[c1] != c2:
                return False
            if c1 not in d and c2 in d.values():
                return False
            d[c1] = c2
            
        return True