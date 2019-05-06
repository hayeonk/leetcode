from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, number):
        self.d[number] += 1
        
    def find(self, value):
        for n in self.d:
            if value - n in self.d:
                if value - n == n and self.d[n] < 2:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)