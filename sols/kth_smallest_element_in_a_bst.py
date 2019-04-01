# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        def count(root):
            if not root:
                return 0
            return 1 + count(root.left) + count(root.right)
        
        leftSize = count(root.left)
        if leftSize == k - 1:
            return root.val
        elif leftSize > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - leftSize)