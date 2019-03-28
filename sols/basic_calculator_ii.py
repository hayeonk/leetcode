class Solution(object):
	def calculate(self, s):
		s = "".join(s.split())
		num = 0
		sign = "+"
		numStack = []
		
		for i in xrange(len(s)):
			if s[i].isdigit():
				num = num*10 + int(s[i])
			if not s[i].isdigit() or i == len(s)-1:
				if sign == "-":
					numStack.append(-num)
				if sign == "+":
					numStack.append(num)
				if sign == "*":
					numStack.append(numStack.pop() * num)
				if sign == "/":
					tmp = numStack.pop()
					if tmp//num < 0 and tmp%num != 0:
						numStack.append(tmp//num+1)
					else:
						numStack.append(tmp//num)
				sign = s[i]
				num = 0
				
		return sum(numStack)