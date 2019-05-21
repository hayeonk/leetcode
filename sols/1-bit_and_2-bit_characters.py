class Solution(object):
    def isOneBitCharacter(self, bits):
        n = len(bits)
        i = 0
        
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        
        return i == n - 1