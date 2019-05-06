from collections import defaultdict
class WordDistance(object):

    def __init__(self, words):
        self.d = defaultdict(list)
        self.n = len(words)
        for i, word in enumerate(words):
            self.d[word].append(i)
        
    def shortest(self, word1, word2):
        ans = self.n
        for i in self.d[word1]:
            for j in self.d[word2]:
                ans = min(ans, abs(i - j))
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)