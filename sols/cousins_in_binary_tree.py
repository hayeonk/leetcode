# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def isCousins(self, root, x, y):
        l = []
        q = deque([(root, 0, None)])
        
        while len(l) < 2:
            node, level, parent = q.popleft()
            if node.val == x or node.val == y:
                l.append([level, parent])
            if node.left:
                q.append([node.left, level+1, node])
            if node.right:
                q.append([node.right, level+1, node])
        
        if l[0][0] == l[1][0] and l[0][1] != l[1][1]:
            return True
        return False
        