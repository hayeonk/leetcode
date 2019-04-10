class Solution(object):
    def findComplement(self, num):
        ans = 0
        i = 0
        while num:
            ans += ((num%2) == 0) << i
            i += 1
            num >>= 1
        return ans