class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))
        
    def get(self):
        if not self.available:
            return -1
        num = self.available.pop()
        return num
    
    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)