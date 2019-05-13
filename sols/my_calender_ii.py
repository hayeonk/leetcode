class MyCalendarTwo(object):
    def __init__(self):
        self.ranges = []
        self.overlap = []

    def book(self, start, end):
        for s, e in self.overlap:
            r1, r2 = self.isOverlap(s, e, start, end)
            if r1 != -1:
                return False
        
        for s, e in self.ranges:
            r1, r2 = self.isOverlap(s, e, start, end)
            if r1 != -1:
                self.overlap.append([r1, r2])
        self.ranges.append([start, end])
        return True
    
    def isOverlap(self, s1, e1, s2, e2):
        if s1 > s2:
            s1, e1, s2, e2 = s2, e2, s1, e1
            
        if e1 <= s2:
            return -1, -1
        
        return s2, min(e1, e2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)