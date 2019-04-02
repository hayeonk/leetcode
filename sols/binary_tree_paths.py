# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        def getPath(root):
            if not root:
                return [[]]
            if not root.left and not root.right:
                return [[root.val]]
            
            ret = []
            if root.left:
                ret += getPath(root.left)
            if root.right:
                ret += getPath(root.right)
            
            for l in ret:
                l.insert(0, root.val)
            return ret
        
        if not root:
            return []
        
        ret = []
        paths = getPath(root)
        for path in paths:
            ret.append("->".join(list(map(str, path))))
        return ret
        