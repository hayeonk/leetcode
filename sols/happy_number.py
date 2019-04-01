class Solution(object):
    def isHappy(self, n):
        d = {}
        num = str(n)
        while num not in d:
            d[num] = 1
            nextNum = 0
            for c in num:
                nextNum += int(c) ** 2
            num = str(nextNum)
        if "1" in d:
            return True
        return False