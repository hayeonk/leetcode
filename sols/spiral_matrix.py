class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        rlo, rhi = 0, len(matrix) - 1
        clo, chi = 0, len(matrix[0]) - 1
        
        ret = []
        
        while rlo <= rhi and clo <= chi:
            if rlo == rhi and clo == chi and matrix[rlo][clo] is not None:
                ret.append(matrix[rlo][clo])
            for j in xrange(clo, chi):
                if matrix[rlo][j] is not None:
                    ret.append(matrix[rlo][j])
                matrix[rlo][j] = None
            for i in xrange(rlo, rhi):
                if matrix[i][chi] is not None:
                    ret.append(matrix[i][chi])
                matrix[i][chi] = None
            for j in xrange(chi, clo, -1):
                if matrix[rhi][j] is not None:
                    ret.append(matrix[rhi][j])
                matrix[rhi][j] = None
            for i in xrange(rhi, rlo, -1):
                if matrix[i][clo] is not None:
                    ret.append(matrix[i][clo])
                matrix[i][clo] = None
            
            rlo, rhi = rlo + 1, rhi - 1
            clo, chi = clo + 1, chi - 1
        
        return ret