# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = Counter()
        ans = []
        
        def serial(node):
            if not node:
                return "#"
            s = "%s.%s.%s" % (str(node.val), serial(node.left), serial(node.right))
            count[s] += 1
            if count[s] == 2:
                ans.append(node)
            return s
        
        serial(root)
        return ans