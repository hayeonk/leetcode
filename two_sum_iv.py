# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        def find(root, k, found):
            if not root:
                return False
            if k - root.val in found:
                return True
            found.add(root.val)
            return find(root.left, k, found) or find(root.right, k, found)
        return find(root, k, set())