from collections import defaultdict
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        d = defaultdict(list)
        for i, word in enumerate(words):
            d[word].append(i)
        
        ans = len(words)
        
        for i in d[word1]:
            for j in d[word2]:
                ans = min(ans, abs(i - j))
        
        return ans