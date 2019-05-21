from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        C1 = Counter(secret)
        C2 = Counter(guess)
        bulls = cows = 0
        for c in C2:
            cows += min(C2[c], C1[c])
        
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                cows -= 1
        
        return "%dA%dB" % (bulls, cows)