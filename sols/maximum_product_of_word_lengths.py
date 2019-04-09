class Solution(object):
    def maxProduct(self, words):
        d = {}
        for c, n in zip (list("abcdefghijklmnopqrstuvwxyz"), range(26)):
            d[c] = n
        
        def toNum(word):
            num = 0
            for c in word:
                num |= (1 << d[c])
            
            return num
        
        B = [0] * len(words)
        for i, word in enumerate(words):
            B[i] = toNum(word)
            words[i] = len(word)
        
        maxVal = 0
        for i, w1 in enumerate(B):
            for j, w2 in enumerate(B):
                if w1 & w2 == 0:
                    maxVal = max(maxVal, words[i] * words[j])
        return maxVal
                    