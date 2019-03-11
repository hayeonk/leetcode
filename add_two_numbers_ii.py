# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def add(l1, l2):
            if l1 == None and l2 == None:
                return None, 0
            ret, carry = add(l1.next, l2.next)
            val = carry + l1.val + l2.val
            fullResult = ListNode(val % 10)
            fullResult.next = ret
            return fullResult, val / 10
        
        def padList(l, pad):
            for i in xrange(pad):
                node = ListNode(0)
                node.next = l
                l = node
            return l
        
        def length(l):
            if l == None:
                return 0
            return 1 + length(l.next)
        
        len1 = length(l1)
        len2 = length(l2)
        
        if len1 < len2:
            l1 = padList(l1, len2 - len1)
        else:
            l2 = padList(l2, len1 - len2)
        
        ret, carry = add(l1, l2)
        if not carry:
            return ret
        result = ListNode(carry)
        result.next = ret
        return result