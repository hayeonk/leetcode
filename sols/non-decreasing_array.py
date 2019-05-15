class Solution(object):
    def checkPossibility(self, nums):
        def check(A):
            for i in xrange(len(A)-1):
                if A[i] > A[i+1]:
                    return False
            return True
        
        n = len(nums)
        for i in xrange(n-1):
            if nums[i] > nums[i+1]:
                A = list(nums)
                A[i] = nums[i+1]
                if check(A):
                    return True
                A = list(nums)
                A[i+1] = nums[i]
                if check(A):
                    return True
                
                return False
        
        return True