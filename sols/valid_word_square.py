class Solution(object):
    def validWordSquare(self, words):
        n = len(words)
        for i in xrange(n):
            for j in xrange(len(words[i])):
                if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True