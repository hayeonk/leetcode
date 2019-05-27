class RLEIterator(object):
    def __init__(self, A):
        self.A = A
        self.idx = 0
        self.p = 0

    def next(self, n):
        self.p += n
        while self.idx < len(self.A) and self.p > self.A[self.idx]:
            self.p -= self.A[self.idx]
            self.idx += 2
        
        if self.idx >= len(self.A):
            return -1
            
        return self.A[self.idx+1]
    
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)