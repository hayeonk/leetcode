class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum(map(int, [c for c in str(num)]))
        return num