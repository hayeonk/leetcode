class Solution(object):
    def minKBitFlips(self, A, K):
        n = len(A)
        hint = [0] * n
        ans = flip = 0
        
        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:
                ans += 1
                if i + K > n:
                    return -1
                
                flip ^= 1
                if i + K < n:
                    hint[i+K] ^= 1
        
        return ans