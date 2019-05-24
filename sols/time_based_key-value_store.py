from collections import defaultdict
from bisect import *
class TimeMap(object):

    def __init__(self):
        self.keys = defaultdict(list)
        self.keyTime = {}

    def set(self, key, value, timestamp):
        insort(self.keys[key], timestamp)
        self.keyTime[(key, timestamp)] = value

    def get(self, key, timestamp):
        idx = bisect(self.keys[key], timestamp)
        if idx == 0:
            return ""
        
        time = self.keys[key][idx-1]
        return self.keyTime[(key, time)]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)