from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        d = defaultdict(set)
        for w1, w2 in pairs:
            d[w1].add(w2)
            d[w2].add(w1)
        
        if len(words1) != len(words2):
            return False
        
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w2 in d[w1]:
                continue
            return False
        return True