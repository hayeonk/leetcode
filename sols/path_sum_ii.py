# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if root.val == sum and not root.left and not root.right:
            return [[root.val]]
        
        l = self.pathSum(root.left, sum - root.val)
        r = self.pathSum(root.right, sum - root.val)
        ret = l + r
        for x in ret:
            x.insert(0, root.val)
        return ret