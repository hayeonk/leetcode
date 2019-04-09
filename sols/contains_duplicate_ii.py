class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        d = set()
        
        for i in xrange(min(n, k + 1)):
            if nums[i] in d:
                return True
            d.add(nums[i])
        
        for i in xrange(k + 1, n):
            d.remove(nums[i-k-1])
            if nums[i] in d:
                return True
            d.add(nums[i])
        
        return False