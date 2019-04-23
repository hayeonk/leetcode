# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        
        maxIdx = 0
        for i in xrange(len(nums)):
            if nums[i] > nums[maxIdx]:
                maxIdx = i
        
        root = TreeNode(nums[maxIdx])
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root