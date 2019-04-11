class Solution(object):
    def multiply(self, num1, num2):
        d = {}
        s = "0123456789"
        for c, n in zip(s, range(10)):
            d[c] = n
        
        ans = 0
        mult = 1
        for c2 in reversed(num2):
            num = 0
            m = 1
            for c1 in reversed(num1):
                num += d[c1] * d[c2] * m
                m *= 10
            ans += num * mult
            mult *= 10
        return str(ans)