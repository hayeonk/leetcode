class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in xrange(32):
            ret <<= 1
            ret += n%2
            n /= 2
        return ret