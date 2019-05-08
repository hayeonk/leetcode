class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        oneLen = prevLen = 0
        ans = 0
        oneZero = False
        
        for n in nums:
            if n == 1:
                oneLen += 1
            else:
                if not oneZero:
                    prevLen = oneLen
                    oneLen += 1
                    oneZero = True
                else:
                    oneLen = oneLen - prevLen
                    prevLen = oneLen - 1
            ans = max(ans, oneLen)
        return ans