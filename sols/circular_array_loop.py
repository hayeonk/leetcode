class Solution(object):
    def circularArrayLoop(self, nums):
        def isCycle(start):
            l = {}
            n = len(nums)
            idx = start
            while idx not in l:
                l[idx] = nums[idx]
                idx = (idx + nums[idx]) % n
            
            directions = len([l[k] for k in l if l[k] > 0])                
            if start == idx and len(l) > 1 and (directions == len(l) or directions == 0):
                return True
            return False
            
        for i in xrange(len(nums)):
            if isCycle(i):
                return True
        return False