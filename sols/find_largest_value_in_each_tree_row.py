# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        ret = []
        
        def getMax(root, level):
            if not root:
                return
            if len(ret) <= level:
                ret.append(root.val)
            else:
                ret[level] = max(ret[level], root.val)
            
            getMax(root.left, level + 1)
            getMax(root.right, level + 1)
        
        getMax(root, 0)
        return ret