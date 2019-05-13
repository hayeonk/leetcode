from collections import defaultdict
class MyCalendarThree(object):
    def __init__(self):
        self.delta = defaultdict(int)

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1
        
        ans = 0
        k = 0
        for d in sorted(self.delta):
            k += self.delta[d]
            ans = max(ans, k)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)