class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [0] * (k + 1)
        self.front = self.rear = 0
        self.n = k + 1

    def enQueue(self, value):
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.n
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.n
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]
        
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[(self.rear-1) % self.n]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.n == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()