from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, A, B):
        f = Counter(A.split()) + Counter(B.split())
        
        return [word for word in f if f[word] == 1]