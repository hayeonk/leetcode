class Solution(object):
    def hasAlternatingBits(self, n):
        isOne = n % 2
        while n > 0:
            n /= 2
            if n % 2 == isOne:
                return False
            isOne = n % 2
        return True