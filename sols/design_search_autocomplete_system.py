from collections import defaultdict
from heapq import *
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.prefix = defaultdict(list)
        self.count = defaultdict(int)
        self.curString = ""
        
        for s, n in zip(sentences, times):
            self.count[s] = n
            for i in xrange(1, len(s)+1):
                heappush(self.prefix[s[:i]], (-n, s))

    def input(self, c):
        if c == "#":
            self.count[self.curString] += 1
            for i in xrange(1, len(self.curString)+1):
                heappush(self.prefix[self.curString[:i]], (-self.count[self.curString], self.curString))
                
            self.curString = ""
            
        else:
            self.curString += c
            ret = []
            tmp = []
            while self.prefix[self.curString] and len(ret) < 3:
                freq, s = heappop(self.prefix[self.curString])
                if s in ret:
                    continue
                ret.append(s)
                tmp.append((freq, s))
            for f, s in tmp:
                heappush(self.prefix[self.curString], (f, s))
            return ret
            
            
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)