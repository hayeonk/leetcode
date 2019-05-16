"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        if not node:
            return node
        
        if node.right:
            succ = node.right
            while succ.left:
                succ = succ.left
            return succ
        
        while node.parent and node.parent.val < node.val:
            node = node.parent
        
        return node.parent