# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        leaves = set()
        self.knode = None
        
        def traverse(root, path):
            if not root:
                return
            
            if root.val == k:
                self.knode = path
            
            if not root.left and not root.right:
                leaves.add((path, root.val))
            
            traverse(root.left, path + "L")
            traverse(root.right, path + "R")
        
        traverse(root, "")
        
        def getDistance(knode, leaf):
            i = 0
            for i in xrange(min(len(knode), len(leaf)) + 1):
                if i >= len(knode) or i >= len(leaf) or knode[i] != leaf[i]:
                    break
            
            return len(knode[i:]) + len(leaf[i:])
        
        ans = float('inf')
        minDistVal = None
        print leaves
        for leaf, val in leaves:
            d = getDistance(self.knode, leaf)
            if d < ans:
                ans = d
                minDistVal = val
            
        return minDistVal