class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        
        lengths = [0] * n
        counts = [1] * n
        
        for j, num in enumerate(nums):
            for i in xrange(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        
        return sum(c for i, c in enumerate(counts) if lengths[i] == max(lengths))