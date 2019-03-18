# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        runner = dummy
        
        for i in xrange(n + 1):
            runner = runner.next
        
        while runner != None:
            prev = prev.next
            runner = runner.next
        prev.next = prev.next.next
        return dummy.next