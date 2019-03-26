from collections import defaultdict

class Trie(object):

    def __init__(self):
        self.children = {}
        self.terminates = False

    def insert(self, word):
        if not word:
            return
        
        c = word[0]
        if c not in self.children:
            self.children[c] = Trie()
        
        if len(word) > 1:
            self.children[c].insert(word[1:])
        else:
            self.children[c].terminates = True

    def search(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        if node.terminates:
            return True
        return False

    def startsWith(self, prefix):
        node = self.children
        for c in prefix:
            if c not in node:
                return False
            node = node[c].children
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)