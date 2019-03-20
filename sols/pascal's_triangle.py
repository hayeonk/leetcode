class Solution(object):
    def generate(self, numRows):
        ret = []
        for i in xrange(numRows):
            curRow = []
            for j in xrange(i):
                if j == 0:
                    curRow += [1]
                else:
                    curRow += [ret[i-1][j-1] + ret[i-1][j]]
            
            curRow += [1]
            ret.append(curRow)
        
        return ret