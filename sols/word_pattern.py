class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split()
        if len(pattern) != len(words):
            return False
        
        d = {}
        for c, word in zip(list(pattern), words):
            if c in d and d[c] != word:
                return False
            
            if c not in d and word in d.values():
                return False
            
            d[c] = word
        
        return True
        