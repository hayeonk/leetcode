class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        
        n = len(triangle)
        for i in reversed(xrange(n-1)):
            for j in xrange(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]