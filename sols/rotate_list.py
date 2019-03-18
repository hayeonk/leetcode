# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        length = 0
        
        while fast.next:
            length += 1
            fast = fast.next
            
        for i in xrange(length - k%length):
            slow = slow.next
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        
        return dummy.next