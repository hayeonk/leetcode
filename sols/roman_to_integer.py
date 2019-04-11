class Solution(object):
    def romanToInt(self, s):
        sym = "IVXLCDM"
        num = [1, 5, 10, 50, 100, 500, 1000]
        d = {}
        for c, n in zip(sym, num):
            d[c] = n
        
        n = len(s)
        i = ans = 0
        while i < n:
            if i < n-1 and s[i:i+2] in ("IV", "IX", "XL", "XC", "CD", "CM"):
                ans += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans