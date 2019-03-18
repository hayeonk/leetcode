# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        def pathFrom(root, sum):
            if not root:
                return 0
            ret = pathFrom(root.left, sum - root.val) + pathFrom(root.right, sum - root.val)
            return ret + 1 if root.val == sum else ret
            
        if not root:
            return 0
        return pathFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)