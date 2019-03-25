class Solution(object):
    def clumsy(self, N):
        def getThree(N):
            if N <= 1:
                return 1
            if N == 2:
                return 2 * 1
            if N == 3:
                return 3 * 2
            return N * (N-1) / (N-2)
        
        s = 1
        ret = 0
        while N > 3:
            ret += s * getThree(N) + (N-3)
            s = -1
            N -= 4
        if N:
            ret += s * getThree(N)
        return ret