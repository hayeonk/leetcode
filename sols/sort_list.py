# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        def merge(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            
            dummy = ListNode(0)
            ptr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    ptr.next = l1
                    l1 = l1.next
                    ptr = ptr.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                    ptr = ptr.next
            if l1:
                ptr.next = l1
                
            if l2:
                ptr.next = l2
            
            return dummy.next
        
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = self.sortList(slow.next)
        slow.next = None
        l1 = self.sortList(head)
        return merge(l1, l2)