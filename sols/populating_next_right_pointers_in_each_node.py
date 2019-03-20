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
        
        def connectNode(p, q):
            if not p:
                return
            
            p.next = q
            connectNode(p.left, p.right)
            connectNode(p.right, q.left)
            connectNode(q.left, q.right)
        
        connectNode(root.left, root.right)
        return root