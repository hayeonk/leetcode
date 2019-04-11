# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        def getLength(head):
            if not head:
                return 0
            return 1 + getLength(head.next)
        
        if k == 1 or getLength(head) < k:
            return head
        
        prev = prevprev = head
        cur = head.next
        for i in xrange(k-1):
            prev.next = cur.next
            cur.next = prevprev
            prevprev = cur
            cur = prev.next
            if i == k-2:
                prev.next = self.reverseKGroup(cur, k)
        
        return prevprev