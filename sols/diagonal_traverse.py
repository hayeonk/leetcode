class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        
        def leftdown(i, j):
            if i == n-1 and j == m-1:
                if ans[-1] != matrix[i][j]:
                    ans.append(matrix[i][j])
                return
            
            while 0 <= i < n and 0 <= j < m:
                ans.append(matrix[i][j])
                i += 1
                j -= 1
            i -= 1
            j += 1
            if i < n-1:
                rightup(i+1, j)
            else:
                rightup(i, j+1)
        
        def rightup(i, j):
            if i == n-1 and j == m-1:
                if not ans or ans[-1] != matrix[i][j]:
                    ans.append(matrix[i][j])
                return
            
            while 0 <= i < n and 0 <= j < m:
                ans.append(matrix[i][j])
                i -= 1
                j += 1
            i += 1
            j -= 1
            if j < m-1:
                leftdown(i, j+1)
            else:
                leftdown(i+1, j)
                
        rightup(0, 0)
        return ans