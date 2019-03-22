class Solution(object):
    def numberToWords(self, num):
        D = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        X = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        T = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        XX = "Hundred"
        XXX = "Thousand"
        M = "Million"
        B = "Billion"
        
        def three(num):
            s = []
            if num >= 100:
                s += [D[num/100], XX]
                num %= 100
            if num >= 20:
                s += [X[num/10]]
                num %=10
            if num >= 10:
                s += [T[num%10]]
                num = 0
            if num > 0:
                s += [D[num]]
            return s
        if num == 0:
            return "Zero"
        s = []
        if num >= 10**9:
            s += [D[num/(10**9)], B]
            num %= 10**9
        if num >= 10**6:
            s += three(num/(10**6)) + [M]
            num %= 10**6
        if num >= 10**3:
            s += three(num/(10**3)) + [XXX]
            num %= 10**3
        s += three(num)
        return " ".join(s)
            