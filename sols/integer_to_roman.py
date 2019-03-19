class Solution(object):
    def intToRoman(self, num):
        ret = ""
        if num >= 1000:
            ret += "M" * (num / 1000)
            num %= 1000
        if num >= 900:
            ret += "CM"
            num %= 900
        if num >= 500:
            ret += "D"
            num -= 500
        if num >= 400:
            ret += "CD"
            num -= 400
        if num >= 100:
            ret += "C" * (num / 100)
            num %= 100
        if num >= 90:
            ret += "XC"
            num %= 90
        if num >= 50:
            ret += "L"
            num -= 50
        if num >= 40:
            ret += "XL"
            num -= 40
        if num >= 10:
            ret += "X" * (num / 10)
            num %= 10
        if num >= 9:
            ret += "IX"
            num %= 9
        if num >= 5:
            ret += "V"
            num -= 5
        if num >= 4:
            ret += "IV"
            num -= 4
        if num >= 1:
            ret += "I" * (num)
        
        return ret