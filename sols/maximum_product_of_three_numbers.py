class Solution(object):
    def maximumProduct(self, nums):
        minus = [x for x in nums if x < 0]
        plus = [x for x in nums if x > 0]
        
        minus.sort()
        plus.sort()
        
        ans = nums[0] * nums[1] * nums[2]
        if len(plus) >= 3:
            ans = max(ans, plus[-1] * plus[-2] * plus[-3])
        if len(minus) >= 2 and len(plus) >= 1:
            ans = max(ans, minus[0] * minus[1] * plus[-1])
        return ans