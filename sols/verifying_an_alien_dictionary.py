class Solution(object):
    def isAlienSorted(self, words, order):
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        
        for i in xrange(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            check = False
            for j in xrange(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    c1 = word1[j]
                    c2 = word2[j]
                    check = True
                    
                    if d[c2] < d[c1]:
                        return False
                    break
            if not check and len(word1) > len(word2):
                return False
            
        return True