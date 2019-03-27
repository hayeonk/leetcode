class Solution(object):
    def exist(self, board, word):
        if not word:
            return True
        if not board or not board[0]:
            return False
        
        n = len(board)
        m = len(board[0])
        
        def find(i, j, word):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True
            tmp = board[i][j]
            board[i][j] = "*"
            res = find(i+1, j, word[1:]) or find(i-1, j, word[1:]) or find(i, j+1, word[1:]) or find(i, j-1, word[1:])
            board[i][j] = tmp
            return res
        
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == word[0]:
                    if find(i, j, word,):
                        return True
        return False