class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        x = int("".join(reversed(str(abs(x))))) * sign
        return x if -(1<<31) <= x < (1<<31) else 0