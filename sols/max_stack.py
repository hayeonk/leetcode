class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.maxVal = [-float('inf')]

    def push(self, x):
        self.stack.append(x)
        self.maxVal.append(max(self.maxVal[-1], x))
        
    def pop(self):
        self.maxVal.pop()
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxVal[-1]
    
    def popMax(self):
        tmp = []
        maxVal = self.maxVal[-1]
        while self.stack[-1] != maxVal:
            tmp.append(self.stack.pop())
            self.maxVal.pop()
        self.stack.pop()
        self.maxVal.pop()
        
        while tmp:
            self.stack.append(tmp.pop())
            self.maxVal.append(max(self.maxVal[-1], self.stack[-1]))
            
        return maxVal

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()