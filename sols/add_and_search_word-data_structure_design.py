class Node(object):
    def __init__(self):
        self.terminate = False
        self.children = {}
        
class WordDictionary(object):
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.terminate = True
        
    def search(self, word):
        return self.searchHelper(self.root, word)
    
    def searchHelper(self, node, word):
        for i in xrange(len(word)):
            c = word[i]
            if c != ".":
                if c not in node.children:
                    return False
                node = node.children[c]
            else:
                for ch in node.children:
                    if self.searchHelper(node.children[ch], word[i+1:]):
                        return True
                return False
        
        return node.terminate

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)