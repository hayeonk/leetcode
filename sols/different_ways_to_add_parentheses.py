class Solution(object):
    def diffWaysToCompute(self, exp):
        def calculate(num1, num2, sign):
            if sign == "+":
                return num1 + num2
            elif sign == "-":
                return num1 - num2
            else:
                return num1 * num2
        
        ans = []
        for i in xrange(len(exp)):
            if not exp[i].isdigit():
                left = self.diffWaysToCompute(exp[:i])
                right = self.diffWaysToCompute(exp[i+1:])
                
                for n1 in left:
                    for n2 in right:
                        ans.append(calculate(n1, n2, exp[i]))
        if not ans:
            return [int(exp)]
        return ans