class Solution(object):
    def monotoneIncreasingDigits(self, N):
        N = map(int, str(N))
        start = 0
        for i in xrange(1, len(N)):
            if N[i-1] < N[i]:
                start = i
            elif N[i-1] > N[i]:
                break
        if start == len(N)-1:
            return int("".join(map(str, N)))
    
        N[start] -= 1
        for i in xrange(start+1, len(N)):
            N[i] = 9
        return int("".join(map(str, N)))