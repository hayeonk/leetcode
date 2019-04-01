import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        
        push(0, 0)
        pair = []
        
        while len(pair) < k and queue:
            _, i, j = heapq.heappop(queue)
            pair.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)
        return pair