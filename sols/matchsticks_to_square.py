class Solution(object):
    def makesquare(self, nums):
        if len(nums) < 4 or sum(nums) % 4 != 0:
            return False
        
        length = sum(nums) / 4
        if max(nums) > length:
            return False
        
        nums.sort(reverse=True)
        def canMake(idx, lengths):
            if idx == len(nums):
                return True
            
            for i in xrange(4):
                if lengths[i] + nums[idx] <= length:
                    lengths[i] += nums[idx]
                    if canMake(idx+1, lengths):
                        return True
                    lengths[i] -= nums[idx]
                
            return False
    
        return canMake(0, [0, 0, 0, 0])