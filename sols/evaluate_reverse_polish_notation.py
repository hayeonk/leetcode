class Solution(object):
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        
        stack = []
        for c in tokens:
            try:
                int(c)
                stack.append(int(c))
            except:
                n2 = stack.pop()
                n1 = stack.pop()
                if c == "+":
                    stack.append(n1 + n2)
                if c == "-":
                    stack.append(n1 - n2)
                if c == "*":
                    stack.append(n1 * n2)
                if c == "/":
                    if n1 / n2 < 0 and n1 % n2 != 0:
                        stack.append(n1 / n2 + 1)
                    else:
                        stack.append(n1 / n2)
        return stack.pop()