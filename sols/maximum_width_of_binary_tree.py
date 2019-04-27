# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        q = deque([(root, 0, 1)])
        curDepth = ans = 0
        left = 1
        
        while q:
            node, depth, pos = q.popleft()
            if curDepth != depth:
                curDepth = depth
                left = pos
            ans = max(ans, pos - left + 1)
            if node.left:
                q.append((node.left, depth+1, 2*pos))
            if node.right:
                q.append((node.right, depth+1, 2*pos+1))
        
        return ans