from bisect import *
from heapq import *
class Solution(object):
    def smallestRange(self, nums):
        ranges = sorted([num[0] for num in nums])
        ans = [ranges[0], ranges[-1]]
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num[0], i))
        
        while pq:
            minV, idx = heappop(pq)
            
            nums[idx].pop(0)
            if nums[idx]:
                insort(ranges, nums[idx][0])
                ranges.remove(minV)
                heappush(pq, (nums[idx][0], idx))
            
            if ranges[-1] - ranges[0] < ans[1] - ans[0]:
                ans = [ranges[0], ranges[-1]]
        return ans