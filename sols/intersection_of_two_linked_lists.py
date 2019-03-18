# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        
        len1 = len2 = 0
        l1 = headA; l2 = headB
        
        while l1.next:
            len1 += 1
            l1 = l1.next
        while l2.next:
            len2 += 1
            l2 = l2.next
        
        if l1 != l2:
            return None
        
        if len1 > len2:
            for i in xrange(len1 - len2):
                headA = headA.next
        else:
            for i in xrange(len2 - len1):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next