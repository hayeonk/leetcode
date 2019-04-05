class Solution(object):
    def superPow(self, a, b):
        b = int("".join(map(str, b)))
        d = []
        num = a
        
        while b > 0:
            num %= 1337
            b -= 1
            if num in d:
                break
            d += [num]
            num *= a
        
        if b == 0:
            return num / a
        return d[(b)%len(d)]