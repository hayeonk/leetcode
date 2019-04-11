from collections import Counter
class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            if max([0] + Counter([x for x in row if x != "."]).values()) >= 2:
                return False
        
        for col in zip(*board):
            if max([0] + Counter([x for x in col if x != "."]).values()) >= 2:
                return False
        
        idx = [0, 3, 6, 9]
        for i in xrange(3):
            for j in xrange(3):
                s = ""
                for row in board[idx[i]:idx[i+1]]:
                    s += "".join(row[idx[j]:idx[j+1]])
                if max([0] + Counter([x for x in s if x != "."]).values()) >= 2:
                    return False
        return True