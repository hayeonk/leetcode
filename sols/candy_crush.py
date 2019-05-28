class Solution(object):
    def candyCrush(self, board):
        n = len(board)
        m = len(board[0])
        
        def dfs(i, j, di, dj, recStack):
            recStack.add((i, j))
            
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and abs(board[i][j]) == abs(board[ni][nj]):
                dfs(ni, nj, di, dj, recStack)
            
            return recStack            
            
        def markCrushCandy(board):
            check = False
            
            for i in xrange(n):
                for j in xrange(m):
                    hori = dfs(i, j, 0, 1, set())
                    vert = dfs(i, j, 1, 0, set())
                    if len(hori) >= 3 and board[i][j] != 0:
                        check = True
                        for x, y in hori:
                            board[x][y] = -abs(board[x][y])
                    if len(vert) >= 3 and board[i][j] != 0:
                        check = True
                        for x, y in vert:
                            board[x][y] = -abs(board[x][y])
            return check
        
        def removeCandy(board):
            for col in xrange(m):
                i = n - 1
                for j in xrange(n-1, -1, -1):
                    if board[j][col] > 0:
                        board[i][col] = board[j][col]
                        i -= 1
                for j in xrange(i, -1, -1):
                    board[j][col] = 0
                    
        while True:
            check = markCrushCandy(board)
            if not check:
                break
            removeCandy(board)
            
        return board