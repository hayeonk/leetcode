from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        n = len(hand)
        if n % W != 0:
            return False
        
        C = Counter(hand)
        while C:
            minVal = min(C.keys())
            for i in xrange(W):
                if C[minVal+i] <= 0:
                    return False
                C[minVal+i] -= 1
                if C[minVal+i] == 0:
                    del C[minVal+i]
        return True