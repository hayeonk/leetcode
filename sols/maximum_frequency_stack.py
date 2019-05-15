from collections import defaultdict
class FreqStack(object):
    def __init__(self):
        self.freq = defaultdict(list)
        self.count = defaultdict(int)
        
    def push(self, x):
        self.count[x] += 1
        self.freq[self.count[x]].append(x)
        
    def pop(self):
        maxFreq = max(self.freq.keys())
        n = self.freq[maxFreq].pop()
        if not self.freq[maxFreq]:
            del self.freq[maxFreq]
            
        self.count[n] -= 1
            
        return n

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()