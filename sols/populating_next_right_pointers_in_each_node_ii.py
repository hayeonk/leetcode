"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        
        def connectTree(nodes):
            if not nodes:
                return
            
            nextNodes = []
            for i in xrange(len(nodes)-1):
                nodes[i].next = nodes[i+1]
            for i in xrange(len(nodes)):
                if nodes[i].left:
                    nextNodes += [nodes[i].left]
                if nodes[i].right:
                    nextNodes += [nodes[i].right]
            connectTree(nextNodes)
        
        nodes = []
        if root.left:
            nodes += [root.left]
        if root.right:
            nodes += [root.right]
        connectTree(nodes)
        return root