# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        def getLength(root):
            if not root:
                return 0
            return 1 + getLength(root.next)
        
        def cutLength(root, length):
            if length == 0:
                return None, root
            
            node = root
            for i in xrange(length - 1):
                node = node.next
            tmp = node.next
            node.next = None
            
            return root, tmp
            
        n = getLength(root)
        cnt = n / k
        ans = []
        nextNode = root
        
        for i in xrange(n%k):
            node, nextNode = cutLength(nextNode, cnt + 1)
            ans.append(node)
            
        for i in xrange(n%k, k):
            node, nextNode = cutLength(nextNode, cnt)
            ans.append(node)
        return ans