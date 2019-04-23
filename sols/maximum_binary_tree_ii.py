# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root