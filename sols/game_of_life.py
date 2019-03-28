class Solution(object):
    def gameOfLife(self, board):
        if not board:
            return
        
        def count(i, j):
            dxdy = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
            ret = 0
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and board[x][y] in live:
                    ret += 1
            return ret
            
        live = [1, 2]
        dead = [0, 3]
        
        n = len(board)
        m = len(board[0])
        
        for i in xrange(n):
            for j in xrange(m):
                cnt = count(i, j)
                if board[i][j] in live:
                    if cnt not in [2, 3]:
                        board[i][j] = 2
                else:
                    if cnt == 3:
                        board[i][j] = 3
        
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1