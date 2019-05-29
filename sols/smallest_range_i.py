class Solution(object):
    def smallestRangeI(self, A, K):
        minV, maxV = min(A), max(A)
        return max(0, maxV - minV - 2 * K)