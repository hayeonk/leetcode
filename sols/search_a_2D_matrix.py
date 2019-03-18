class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        lo = 0
        hi = m - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        matrix = matrix[hi]
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False