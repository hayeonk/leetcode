# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        ret = []
        def traverse(root, level):
            if not root:
                return
            
            if len(ret) <= level:
                ret.append([root.val])
            else:
                ret[level].append(root.val)
            
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        
        traverse(root, 0)
        return [float(sum(lev)) / len(lev) for lev in ret]