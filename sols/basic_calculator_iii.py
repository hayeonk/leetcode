class Solution(object):
    def calculate(self, s):
        s = "".join(s.split())
        stack = []
        num = 0
        sign = "+"
        
        def calc(sign, num):
            if sign == "+":
                return num
            elif sign == "-":
                return -num
            elif sign == "*":
                return num * stack.pop()
            else:
                n = stack.pop()
                if n / num < 0 and n % num:
                    return n / num + 1
                else:
                    return n / num
                
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "(":
                stack.append(sign)
                stack.append("(")
                sign = "+"
                num = 0
            elif c == ")":
                nums = []
                nums.append(calc(sign, num))
                n = stack.pop()
                while n != "(":
                    nums.append(n)
                    n = stack.pop()
                stack.append(calc(stack.pop(), sum(nums)))
                num = 0
                sign = "+"
            else:
                if num:
                    stack.append(calc(sign, num))
                sign = c
                num = 0
            
        stack.append(calc(sign, num))
        return sum(stack)