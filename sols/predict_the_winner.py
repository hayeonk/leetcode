class Solution(object):
    def PredictTheWinner(self, nums):
        def canWin(nums, myScore, otherScore):
            n = len(nums)
            if n == 0:
                return myScore >= otherScore
        
            return not (canWin(nums[1:], otherScore, myScore + nums[0]) and canWin(nums[:-1], otherScore, myScore + nums[-1]))
        
        if len(nums) <= 1:
            return True
        return canWin(nums, 0, 0)