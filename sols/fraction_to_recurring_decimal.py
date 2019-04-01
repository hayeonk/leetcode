class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        ret = ""
        sign = numerator * denominator < 0
        if sign:
            ret += "-"
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ret += str(numerator / denominator)
        
        numerator = (numerator % denominator) * 10
        if numerator == 0:
            return ret
        
        ret += "."
        fraction = []
        repeat = -1
        while numerator:
            n = str(numerator / denominator)
            if (n, numerator) in fraction:
                repeat = fraction.index((n, numerator))
                break
            fraction.append((n, numerator))
            numerator = (numerator % denominator) * 10
        
        fraction = [x for x, y in fraction]
        if repeat == -1:
            ret += "".join(fraction)
        else:
            ret += "%s(%s)" % ("".join(fraction[:repeat]), "".join(fraction[repeat:]))
            
        return ret