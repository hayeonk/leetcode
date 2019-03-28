# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        ret = []
        
        def zigzag(root, level):
            if not root:
                return
            
            while len(ret) <= level:
                ret.append([])
            
            if level%2 == 0:
                ret[level].append(root.val)
            else:
                ret[level].insert(0, root.val)
            
            zigzag(root.left, level + 1)
            zigzag(root.right, level + 1)
            
        zigzag(root, 0)
        return ret