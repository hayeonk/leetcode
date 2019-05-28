class Solution(object):
    def splitArray(self, nums):
        if not nums:
            return False
        
        n = len(nums)
        psum = [nums[0]]
        for i in xrange(1, n):
            psum.append(psum[-1] + nums[i])
        
        for j in xrange(3, n - 3):
            sumSet = set()
            for i in xrange(1, j - 1):
                if psum[i-1] == psum[j-1] - psum[i]:
                    sumSet.add(psum[i-1])
            
            for k in xrange(j + 2, n - 1):
                if psum[n-1] - psum[k] == psum[k-1] - psum[j] and psum[n-1] - psum[k] in sumSet:
                    return True
        
        return False