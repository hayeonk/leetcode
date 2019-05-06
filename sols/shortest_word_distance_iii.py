from collections import defaultdict
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        d = defaultdict(list)
        for i, word in enumerate(words):
            d[word].append(i)
            
        ans = float('inf')
        if word1 == word2:
            l = d[word1]
            for i in xrange(len(l)-1):
                ans = min(ans, l[i+1] - l[i])
            
        else:
            l1, l2 = d[word1], d[word2]
            i = j = 0
            
            while i < len(l1) and j < len(l2):
                ans = min(ans, abs(l1[i] - l2[j]))
                if l1[i] < l2[j]:
                    i += 1
                else:
                    j += 1
        
        return ans