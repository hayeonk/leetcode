# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        
        ret = []
        
        def sumTree(root, cur):
            if not root:
                return
            cur += root.val
            if not root.left and not root.right:
                ret.append(cur)
            else:
                sumTree(root.left, cur*10)
                sumTree(root.right, cur*10)
            
        sumTree(root, 0)
        return sum(ret)