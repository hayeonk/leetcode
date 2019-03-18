# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        ret = []
        def getList(root, level):
            if not root:
                return
            if len(ret) == level:
                ret.append([])
            ret[level].append(root.val)
            getList(root.left, level + 1)
            getList(root.right, level + 1)
        
        getList(root, 0)
        return ret
            