class Node(object):
    def __init__(self):
        self.terminate = False
        self.children = {}

class Solution(object):
    def replaceWords(self, dict, sentence):
        self.root = Node()
        
        def add(word):
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.terminate = True
        
        for word in dict:
            add(word)
        
        ans = sentence.split()
        for i, word in enumerate(ans):
            node = self.root
            for j in xrange(len(word)):
                c = word[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.terminate:
                    ans[i] = word[:j+1]
                    break
            
        return " ".join(ans)