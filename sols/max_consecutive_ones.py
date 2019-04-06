class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums = "".join(map(str, nums)).split("0")
        return len(max(nums, key=len))