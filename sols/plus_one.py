class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        i = n - 1
        
        digits[i] += 1
        carry = digits[i] / 10
        digits[i] %= 10
        i -= 1
        
        while i >= 0 and carry:
            digits[i] += 1
            carry = digits[i] / 10
            digits[i] %= 10
            i -= 1
        
        if carry:
            digits.insert(0, 1)
        return digits
        