# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        
        nodes = range(1, n + 1)

        def genTree(nodes):
            if not nodes:
                return [None]
            ret = []
            for i in xrange(len(nodes)):
                left = genTree(nodes[:i])
                right = genTree(nodes[i+1:])
                for l in range(len(left)):
                    for r in range(len(right)):
                        root = TreeNode(nodes[i])
                        root.left = left[l]
                        root.right = right[r]
                        ret.append(root)
            return ret
        
        return genTree(nodes)
        