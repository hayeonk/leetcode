# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        subtreeSum = []
        
        def getEverySum(node):
            if not node:
                return 0
            subtreeSum.append(getEverySum(node.left) + getEverySum(node.right) + node.val)
            return subtreeSum[-1]
        
        total = getEverySum(root)
        subtreeSum.pop()
        return total / 2.0 in subtreeSum