class Solution(object):
    def matrixReshape(self, nums, r, c):
        if not nums or not nums[0]:
            return nums
        
        n = len(nums)
        m = len(nums[0])
        
        if n * m != r * c:
            return nums
        
        matrix = [[0] * c for _ in xrange(r)]
        row = col = 0
        for i in xrange(n):
            for j in xrange(m):
                matrix[row][col] = nums[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        
        return matrix