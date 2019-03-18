class Solution(object):
    def numTrees(self, n):
        m = [-1] * (n + 1)
        m[0] = m[1] = 1
        
        def getNum(n):
            if m[n] != -1:
                return m[n]
            
            ret = 0
            for i in xrange(n):
                ret += getNum(i) * getNum(n - i - 1)
            m[n] = ret
            return ret
        return getNum(n)