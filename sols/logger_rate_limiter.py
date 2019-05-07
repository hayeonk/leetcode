from collections import defaultdict
class Logger(object):

    def __init__(self):
        self.d = defaultdict(int)
        
    def shouldPrintMessage(self, timestamp, message):
        if message not in self.d:
            self.d[message] = timestamp + 10
            return True
        else:
            if self.d[message] > timestamp:
                return False
            else:
                self.d[message] = timestamp + 10
                return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)