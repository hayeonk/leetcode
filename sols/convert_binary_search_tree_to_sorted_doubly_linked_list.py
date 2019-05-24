"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        def makeDoublyList(root):
            if not root:
                return None, None
            
            leftmostL, rightmostL = makeDoublyList(root.left)
            leftmostR, rightmostR = makeDoublyList(root.right)
            leftmost = rightmost = root
            if rightmostL:
                rightmostL.right = root
                root.left = rightmostL
                leftmost = leftmostL
            if leftmostR:
                leftmostR.left = root
                root.right = leftmostR
                rightmost = rightmostR
            
            return leftmost, rightmost
        
        leftmost, rightmost = makeDoublyList(root)
        if leftmost is None:
            return None
        
        rightmost.right = leftmost
        leftmost.left = rightmost
        return leftmost