import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        queue = []
        
        def push(i, j):
            if i < len(matrix) and j < len(matrix):
                heapq.heappush(queue, [matrix[i][j], i, j])
        
        push(0, 0)
        for _ in xrange(k):
            val, i, j = heapq.heappop(queue)
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)
        return val