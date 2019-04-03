"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        ret = []
        
        def traversal(root, level):
            if not root:
                return 
            if len(ret) <= level:
                ret.append([root.val])
            else:
                ret[level].append(root.val)
            
            for node in root.children:
                traversal(node, level+1)
        
        traversal(root, 0)
        return ret