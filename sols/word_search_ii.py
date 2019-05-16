from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        def dfs(node, i, j, path):
            if node.isWord:
                ans.append(path)
                node.isWord = False
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            
            tmp = board[i][j]
            if tmp not in node.children:
                return
            
            node = node.children[tmp]
            board[i][j] = "*"
            dfs(node, i+1, j, path+tmp)
            dfs(node, i-1, j, path+tmp)
            dfs(node, i, j+1, path+tmp)
            dfs(node, i, j-1, path+tmp)
            board[i][j] = tmp
            
        if not board or not board[0]:
            return []
        
        n = len(board)
        m = len(board[0])
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = []
        node = trie.root
        for i in xrange(n):
            for j in xrange(m):
                dfs(node, i, j, "")
                
        return ans