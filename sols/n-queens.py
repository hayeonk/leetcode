class Solution(object):
    def solveNQueens(self, n):
        ret = []
        def placeQueens(row, columns):
            if row == n:
                ret.append(list(columns))
            else:
                for col in xrange(n):
                    if checkValid(columns, row, col):
                        columns[row] = col
                        placeQueens(row + 1, columns)
        
        def checkValid(columns, row1, col1):
            for row2 in range(row1):
                col2 = columns[row2]
                if col1 == col2:
                    return False
                if abs(col2 - col1) == row1 - row2:
                    return False
            return True
        
        def toBoard(result):
            ret = []
            for res in result:
                board = [["."] * n for _ in xrange(n)]
                for i, j in enumerate(res):
                    board[i][j] = "Q"
                for i, line in enumerate(board):
                    board[i] = "".join(line)
                ret.append(board)
            return ret
                
            
        placeQueens(0, [-1] * n)
        ret = toBoard(ret)
        return ret
        