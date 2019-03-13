# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        
        prev = None 
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
    
        if prev:
            prev.next = None
        
        root = TreeNode(slow.val)
        if slow == head:
            return root
        
        root.right = self.sortedListToBST(slow.next)
        root.left = self.sortedListToBST(head)
        
        return root