from collections import defaultdict
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        
        d = defaultdict(set)
        
        for w1, w2 in pairs:
            d[w1].add(w2)
            d[w2].add(w1)
            
        def dfs(u, dst, visit):
            visit.add(u)
            
            for v in d[u]:
                if v not in visit:
                    if v == dst:
                        return True
                    if dfs(v, dst, visit):
                        return True
            return False
            
        for w1, w2 in zip(words1, words2):
            if w1 == w2 or dfs(w1, w2, set()):
                continue
            return False
        return True