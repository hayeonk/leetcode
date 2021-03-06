from collections import deque
from collections import defaultdict

class Solution(object):
    def solve(self, board):
        if not board:
            return 
        m, n = len(board), len(board[0])
        q = deque([ij for k in range(max(m, n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))])
        while q:
            i, j = q.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                q += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]