class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0
        self.turn = 0

    def next(self):
        if self.turn == 0 and self.i < len(self.v1):
            self.i += 1
            self.turn = 1
            return self.v1[self.i-1]
        if self.turn == 1 and self.j < len(self.v2):
            self.j += 1
            self.turn = 0
            return self.v2[self.j-1]
        
        if self.i < len(self.v1):
            self.i += 1
            return self.v1[self.i-1]
        
        if self.j < len(self.v2):
            self.j += 1
            return self.v2[self.j-1]

    def hasNext(self):
        return self.i < len(self.v1) or self.j < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())