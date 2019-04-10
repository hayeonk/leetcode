class Solution(object):
    def calculate(self, s):
        s = "".join(s.split())
        num = 0
        sign = 1
        stack = []
		
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            else:
                if c == "+":
                    stack.append(sign * num)
                    sign = 1
                elif c == "-":
                    stack.append(sign * num)
                    sign = -1
                elif c == "(":
                    stack.append(sign)
                    stack.append("(")
                    sign = 1
                elif c == ")":
                    tmp = []
                    n = stack.pop()
                    while n != "(":
                        tmp.append(n)
                        n = stack.pop()
                    stack.append(stack.pop() * (sum(tmp) + sign * num))
                num = 0
        
        return sum(stack) + sign * num