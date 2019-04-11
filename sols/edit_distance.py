class Solution(object):
    def minDistance(self, word1, word2):
        m = {}
        
        def solve(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
        
            if (i, j) not in m:
                if word1[i] == word2[j]:
                    ans = solve(i + 1, j + 1)
                else:
                    insert = solve(i, j + 1)
                    delete = solve(i + 1, j)
                    replace = solve(i + 1, j + 1)
                    ans = 1 + min(insert, delete, replace)
                m[(i, j)] = ans
            return m[(i, j)]
        
        return solve(0, 0)