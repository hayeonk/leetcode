class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        rowHasZero = colHasZero = False
        
        for i in range(n):
            if matrix[0][i] == 0:
                rowHasZero = True
        for i in range(m):
            if matrix[i][0] == 0:
                    colHasZero = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if rowHasZero:
            for j in range(n):
                matrix[0][j] = 0
        if colHasZero:
            for i in range(m):
                matrix[i][0] = 0