class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word, pattern):
            if len(word) != len(pattern):
                return False
            
            d = {}
            for c1, c2 in zip(word, pattern):
                if c1 in d and d[c1] != c2:
                    return False
                
                if c1 not in d and c2 in d.values():
                    return False
                
                d[c1] = c2
            
            return True
            
            
        ans = []
        for word in words:
            if match(word, pattern):
                ans.append(word)
        
        return ans