class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        m = len(matrix[0])
        self.psum = [[0] * (m + 1) for _ in xrange(n + 1)]
        for i in xrange(n):
            for j in xrange(m):
                self.psum[i+1][j+1] = self.psum[i+1][j] + self.psum[i][j+1] + matrix[i][j] - self.psum[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        return self.psum[row2+1][col2+1] - self.psum[row1][col2+1] - self.psum[row2+1][col1] + self.psum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)