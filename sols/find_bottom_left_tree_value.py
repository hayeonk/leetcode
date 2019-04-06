# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        stack = []
        height = 0
        ans = [root.val, 0]
        
        while root:
            stack.append((root, height))
            root = root.left
            height += 1
        
        while stack:
            node, h = stack.pop()
            if h > ans[1]:
                ans = [node.val, h]
            
            node = node.right
            h += 1
            
            while node:
                stack.append((node, h))
                node = node.left
                h += 1
        return ans[0]