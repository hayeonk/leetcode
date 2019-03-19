class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -(1<<31) and divisor == -1:
            return (1<<31)-1
        
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        
        while dividend >= divisor:
            temp, m = divisor, 1
            while dividend >= temp << 1:
                temp <<= 1
                m <<= 1
            ret += m
            dividend -= temp
        return ret * sign