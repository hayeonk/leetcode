# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from heapq import *
class Solution(object):
    def closestKValues(self, root, target, k):
        pq = []
        
        def traverse(root, target):
            if not root:
                return
            
            heappush(pq, (abs(root.val - target), root.val))
            
            traverse(root.left, target)
            traverse(root.right, target)
            
        traverse(root, target)
        return [x[1] for x in nsmallest(k, pq)]