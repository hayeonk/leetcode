# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        
        ret = []
        rights = []
        node = root
        while node:
            ret.append(node.val)
            if node.right:
                rights.append(node.right)
            node = node.left
            if not node and rights:
                node = rights.pop()
        return ret