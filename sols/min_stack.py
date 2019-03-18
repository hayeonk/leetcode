class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, x):
        self.stack.append(x)
        if self.minVal:
            x = min(x, self.minVal[-1])
        self.minVal.append(x)        

    def pop(self):
        self.stack.pop()
        self.minVal.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minVal[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()