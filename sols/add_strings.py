class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry = 0
        ans = []
        
        while num1 or num2:
            n1 = ord(num1.pop()) - ord("0") if num1 else 0
            n2 = ord(num2.pop()) - ord("0") if num2 else 0
            add = n1 + n2 + carry
            
            ans.append(add % 10)
            carry = add / 10
        
        if carry:
            ans.append(carry)
            
        return "".join(map(str, ans[::-1]))