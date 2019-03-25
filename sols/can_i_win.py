class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        m = {}
        
        def canWin(nums, total):
            if nums[-1] >= total:
                return True
            
            if tuple(nums) in m:
                return m[tuple(nums)]
            
            for i in xrange(len(nums)):
                if not canWin(nums[:i] + nums[i+1:], total - nums[i]):
                    m[tuple(nums)] = True
                    return True
            m[tuple(nums)] = False
            return False
        
        return canWin(range(1, maxChoosableInteger+1), desiredTotal)