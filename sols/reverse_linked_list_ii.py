# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        end = dummy
        for i in xrange(m - 1):
            end = end.next
        cur = end.next
        fend = cur
        prev = None
        for i in xrange(n - m + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        end.next = prev
        fend.next = tmp
        return dummy.next