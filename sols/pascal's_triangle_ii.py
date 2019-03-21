class Solution(object):
    def getRow(self, rowIndex):
        ret = [1]
        for i in xrange(rowIndex):
            for j in reversed(xrange(1, i+1)):
                ret[j] += ret[j-1]   
            ret += [1]
            
        return ret