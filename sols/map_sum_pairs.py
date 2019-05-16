class TrieNode(object):
    def __init__(self, val):
        self.children = {}
        self.val = val
        
class MapSum(object):
    def __init__(self):
        self.root = TrieNode(0)
        self.d = {}

    def insert(self, key, val):
        if key in self.d:
            newVal = val - self.d[key]
            self.d[key] = val
            val = newVal
        self.d[key] = val
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode(0)
            node.val += val
            node = node.children[c]
        node.val += val
        
    def sum(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)